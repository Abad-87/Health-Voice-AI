import os
from dotenv import load_dotenv

# Load environment variables from .env file (if exists)
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is required. Set it in .env file or environment.")

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
API_KEY = os.getenv("API_KEY", "fallback-secret-key-only-for-testing")

# Optional: helpful for local development
UVICORN_RELOAD = os.getenv("UVICORN_RELOAD", "false").lower() == "true"