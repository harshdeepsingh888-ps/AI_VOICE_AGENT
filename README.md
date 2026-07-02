# AI Voice Agent

An AI-powered voice assistant built with FastAPI, Google Gemini, Whisper, and Edge TTS.

## Features

- Speech-to-Text using OpenAI Whisper
- AI responses using Google Gemini
- Conversation memory
- Text-to-Speech using Edge TTS
- FastAPI backend
- REST API with Swagger documentation

## Tech Stack

- Python 3.12
- FastAPI
- Google Gemini API
- OpenAI Whisper
- PyTorch
- Edge TTS
- FFmpeg
- Pygame

## Project Structure

```
AI_VOICE_AGENT/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── schemas/
│   └── services/
│
├── requirements.txt
├── README.md
└── .env
```

## Run the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn app.main:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

## Current Status

- ✅ Gemini Integration
- ✅ Conversation Memory
- ✅ Whisper Speech-to-Text
- ✅ Edge Text-to-Speech
- ✅ FastAPI Backend