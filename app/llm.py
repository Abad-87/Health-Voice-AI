from openai import OpenAI
from app.config import OPENAI_API_KEY
from typing import List

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are HealthCure AI, a helpful health assistant. ALWAYS include this disclaimer: "I am not a doctor and cannot diagnose or prescribe. Consult a professional for medical advice."
- Be empathetic, calm, polite.
- For symptoms: Suggest general advice (e.g., rest, hydrate) and recommend doctor if severe.
- For medication: Remind dosages if standard, but say "Follow your doctor's instructions."
- For mental health: Offer listening, suggest breathing exercises, recommend professional help.
- Detect emergencies (e.g., chest pain, bleeding): Urge immediate medical help.
- No prescriptions or diagnoses.
- Support multi-turn: Use history.

Response format: Short, natural text only.
"""

def generate_response(query: str, history: List[dict]) -> str:
    try:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history + [{"role": "user", "content": query}]
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return "I'm sorry, I encountered an issue. Please try again. Remember, consult a doctor for health concerns."