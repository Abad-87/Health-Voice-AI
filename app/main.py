from fastapi import FastAPI, WebSocket, UploadFile, File, Depends, HTTPException
from fastapi.responses import StreamingResponse
from app.stt import speech_to_text
from app.llm import generate_response
from app.tts import text_to_speech
from app.memory import get_session_history, save_session_history
from app.schemas import VoiceInput, TextQuery, SessionResponse
from app.utils import check_api_key
import uuid
import io
from typing import Optional

app = FastAPI(title="HealthCure AI")

@app.post("/voice/input")
async def voice_input(file: UploadFile = File(...), session_id: Optional[str] = None, api_key=Depends(check_api_key)):
    try:
        audio_bytes = await file.read()
        text = speech_to_text(audio_bytes)
        return process_query(text, session_id)
    except ValueError as e:
        raise HTTPException(500, str(e))

@app.post("/text/query")
def text_query(query: TextQuery, api_key=Depends(check_api_key)):
    return process_query(query.text, query.session_id)

def process_query(text: str, session_id: Optional[str]):
    session_id = session_id or str(uuid.uuid4())
    history = get_session_history(session_id)
    response_text = generate_response(text, history)
    history.append({"role": "user", "content": text})
    history.append({"role": "assistant", "content": response_text})
    save_session_history(session_id, history)
    audio = text_to_speech(response_text)
    return {"text": response_text, "audio": audio, "session_id": session_id}

@app.get("/session/{session_id}")
def get_session(session_id: str, api_key=Depends(check_api_key)):
    history = get_session_history(session_id)
    return SessionResponse(history=history)

@app.post("/voice/output")
def voice_output(query: TextQuery, api_key=Depends(check_api_key)):
    response_text = generate_response(query.text, [])  # No history for simple output
    audio = text_to_speech(response_text)
    return StreamingResponse(io.BytesIO(audio), media_type="audio/mp3")

@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    audio_buffer = bytearray()
    try:
        while True:
            data = await websocket.receive_bytes()
            if data == b'end':  # Client signals end of speech
                text = speech_to_text(bytes(audio_buffer))
                response = process_query(text, session_id)
                await websocket.send_text(response["text"])
                await websocket.send_bytes(response["audio"])
                audio_buffer.clear()
            else:
                audio_buffer.extend(data)
    except Exception as e:
        await websocket.send_text(f"Error: {str(e)}")
    finally:
        await websocket.close()