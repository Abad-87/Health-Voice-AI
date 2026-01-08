import redis
import json
from app.config import REDIS_URL

r = redis.from_url(REDIS_URL)

def get_session_history(session_id: str) -> list:
    history = r.get(session_id)
    return json.loads(history) if history else []

def save_session_history(session_id: str, history: list):
    r.set(session_id, json.dumps(history), ex=3600)  # Expire in 1 hour