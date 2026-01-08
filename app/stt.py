from openai import OpenAI
from app.config import OPENAI_API_KEY
import io

client = OpenAI(api_key=OPENAI_API_KEY)

def speech_to_text(audio_bytes: bytes) -> str:
    try:
        audio_file = io.BytesIO(audio_bytes)
        audio_file.name = "audio.mp3"
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )
        return transcript
    except Exception as e:
        raise ValueError(f"STT error: {str(e)}")