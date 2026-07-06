# 🤖 AI Voice Agent

A modular AI-powered voice assistant built with Python, Whisper, Gemini, Edge TTS, FastAPI, and WebRTC Voice Activity Detection.

This project is being built step by step with clean architecture, Git versioning, and production-style development practices.

---

## 🚀 Current Version

### ✅ v1.1 — Smart Voice Assistant Core

The assistant can now:

- Listen through microphone
- Detect speech automatically using WebRTC VAD
- Stop recording after silence
- Convert speech to text using Whisper
- Generate AI responses using Gemini
- Maintain conversation memory
- Speak responses using Edge TTS

---

## 🧠 Architecture

```text
User Voice
    ↓
WebRTC VAD Recorder
    ↓
recording.wav
    ↓
Whisper Speech-to-Text
    ↓
Gemini LLM
    ↓
Conversation Memory
    ↓
Edge TTS
    ↓
Speaker Output