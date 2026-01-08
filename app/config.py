import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REDIS_URL = os.getenv("REDIS_URL", "redis://red-d5frc6be5dus73d3jttg:6379")
API_KEY = os.getenv("API_KEY", "7d8703b8809785eaa76d3c09fdf352e3")  # For auth