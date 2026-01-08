# HealthCure AI 🩺🎤

An advanced, safe, and empathetic AI-powered voice agent designed for health-related conversations. HealthCure AI listens to your voice, understands medical intent, provides general health guidance with strict safety guardrails, and responds in a natural, human-like voice.

**Important**: HealthCure AI is **not** a doctor. It never diagnoses conditions, prescribes medication, or replaces professional medical advice.

---

## ✨ Features

- **Real-time Voice Interaction**  
  Speech-to-Text → Intelligent Response → Text-to-Speech (full-duplex feel via WebSocket)
- **Medically Safe Responses**  
  Built-in guardrails: always includes disclaimers, detects emergencies, encourages doctor visits
- **Context-Aware Conversations**  
  Session-based memory using Redis for multi-turn dialogues
- **Natural & Empathetic Tone**  
  Calm, caring, professional voice (OpenAI TTS with "nova" voice)
- **Easy Backend Integration**  
  REST APIs + WebSocket + JSON format + API key authentication
- **Mobile-Friendly Web Interface**  
  Simple mic button for instant voice input
- **Supports Multiple Accents & Noisy Environments**  
  Powered by OpenAI Whisper (excellent with Indian + global English accents)

---

## 🛡️ Safety & Compliance First

- Never makes diagnoses or prescriptions
- Always appends: *"I am not a doctor and cannot diagnose or prescribe. Please consult a professional."*
- Emergency detection (e.g., chest pain, severe symptoms) → urges immediate medical help
- No storage of Protected Health Information (PHI) by default
- Session data expires after 1 hour

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- OpenAI API key (with access to Whisper, GPT-4o-mini, and TTS)
- Redis instance (local or hosted)
- Docker (optional, for easy deployment)

### 1. Clone & Install

```bash
git clone https://github.com/yourusername/healthcure-ai.git
cd healthcure-ai
pip install -r requirements.txt
