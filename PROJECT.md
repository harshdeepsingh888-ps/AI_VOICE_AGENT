# PROJECT.md

# AI Voice Agent

## Project Overview

This project aims to build a production-quality AI Voice Agent similar to ChatGPT Voice Mode or Jarvis. The goal is not only to build a working assistant but also to understand every component involved in modern AI application development.

The project follows an incremental approach where every feature is implemented, tested, documented, and committed before moving to the next milestone.

---

# Tech Stack

- Python 3.12
- FastAPI
- Google Gemini API (gemini-2.5-flash)
- OpenAI Whisper
- PyTorch (CPU)
- Edge TTS
- Pygame
- FFmpeg
- Git & GitHub
- VS Code
- Windows 11

---

# Current Project Structure

```
AI_VOICE_AGENT/

app/
│
├── api/
│   └── chat.py
│
├── core/
│   └── config.py
│
├── schemas/
│   └── chat_schema.py
│
├── services/
│   ├── llm_service.py
│   ├── memory_service.py
│   ├── speech_service.py
│   └── tts_service.py
│
├── main.py
│
README.md
PROJECT.md
requirements.txt
.env
```

---

# Completed Milestones

## Milestone 1 — AI Backend ✅

### Completed

- FastAPI backend created
- Google Gemini integrated
- Conversation memory implemented
- Whisper Speech-to-Text working
- FFmpeg configured
- Edge TTS integrated
- AI responses spoken aloud
- Swagger API tested
- Git repository initialized
- GitHub repository connected
- First milestone committed and pushed

---

# Current Workflow

```
User Input
     │
     ▼
 FastAPI
     │
     ▼
 Gemini
     │
     ▼
 Conversation Memory
     │
     ▼
 Edge TTS
     │
     ▼
 Speaker
```

Whisper has been tested independently and is ready for integration with live microphone input.

---

# Current Status

| Feature | Status |
|----------|--------|
| FastAPI | ✅ |
| Gemini | ✅ |
| Memory | ✅ |
| Whisper | ✅ |
| FFmpeg | ✅ |
| Edge TTS | ✅ |
| GitHub | ✅ |
| API Testing | ✅ |

---

# Current Issues

None.

The application is functioning correctly.

Minor improvements remaining:

- Add `.gitignore`
- Remove generated audio files from Git
- Remove temporary testing scripts
- Refactor TTS integration into cleaner architecture

---

# Next Milestone

## Milestone 2 — Live Voice Conversation

Goal:

```
Press Enter
      │
      ▼
Microphone Recording
      │
      ▼
Whisper
      │
      ▼
Gemini
      │
      ▼
Memory
      │
      ▼
Edge TTS
      │
      ▼
Speaker
```

The assistant should no longer require manually recorded audio files.

---

# Future Roadmap

## Milestone 3

- Continuous conversations
- Push-to-talk
- Better audio recording

## Milestone 4

- Wake word ("Hey Jarvis")
- Voice interruption
- Better personality
- Multiple voices

## Milestone 5

- Persistent database memory
- SQLite/PostgreSQL

## Milestone 6

- Desktop GUI

## Milestone 7

- Web Interface

## Milestone 8

- Docker
- Authentication
- Logging
- Unit Testing
- CI/CD
- Deployment

---

# Development Principles

This project follows these rules:

1. Understand every component before using it.
2. Build one feature at a time.
3. Test every feature before moving forward.
4. Maintain clean architecture.
5. Keep commits small and meaningful.
6. Document every completed milestone.
7. Prioritize learning over speed.

---

# Last Updated

Milestone 1 completed successfully.

The project is now ready to begin live microphone integration.