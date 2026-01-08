from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def text_to_speech(text: str) -> bytes:
    try:
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",  # Natural, caring voice
            input=text
        )
        return response.content
    except Exception as e:
        raise ValueError(f"TTS error: {str(e)}")