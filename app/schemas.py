from pydantic import BaseModel
from typing import Optional, List

class VoiceInput(BaseModel):
    audio: bytes  # Base64 or bytes
    session_id: Optional[str] = None

class TextQuery(BaseModel):
    text: str
    session_id: Optional[str] = None

class SessionResponse(BaseModel):
    history: List[dict]

class VoiceOutput(BaseModel):
    audio: bytes
    text: str