# 🎤 AI Voice Agent

A production-style AI Voice Agent built with **Python**, **Google Gemini**, **Whisper**, **Edge TTS**, and a modular **Agent + Tool Architecture**.

Unlike a traditional voice assistant, this project follows software engineering best practices including modular architecture, plugin-based tools, structured logging, automated testing, Git workflows, and clean separation of responsibilities.

---

# ✨ Features

## 🎙 Voice Interaction

- Speech recognition using OpenAI Whisper
- Voice Activity Detection (WebRTC VAD)
- Natural text-to-speech using Edge TTS
- Hands-free voice conversation

---

## 🧠 AI Agent

- Google Gemini powered reasoning
- Multi-turn conversations
- Conversation memory
- Intelligent tool planning
- Pending request handling

Example:

```
User:
What is the weather?

Agent:
Please tell me the city.

User:
Delhi

Agent:
The current weather in Delhi is...
```

---

## 🔧 Tool System

The agent supports a plugin architecture.

Current tools:

- 🌦 Weather
- 🧮 Calculator
- 🌐 Chrome Launcher
- 📝 Notepad Launcher

Adding a new tool only requires creating a new class inheriting from `BaseTool`.

---

# 🏗 Architecture

```
                    Voice Input
                         │
                         ▼
                 Speech Service
                         │
                         ▼
             Speech Normalizer
                         │
                         ▼
                  Agent Service
              ┌──────────┴──────────┐
              ▼                     ▼
      Gemini Tool Planner     Pending Requests
              │
              ▼
          Tool Manager
              │
          Tool Registry
      ┌───────┼─────────┐
      ▼       ▼         ▼
 Weather   Calculator  Launchers
```

---

# 📂 Project Structure

```
app/
│
├── api/
├── core/
├── schemas/
├── services/
├── tools/
├── utils/
│
tests/
voice_chat.py
```

---

# 🛠 Tech Stack

- Python 3.12
- Google Gemini
- Whisper
- Edge TTS
- WebRTC VAD
- FastAPI
- PyGame
- PyTest

---

# 🧪 Testing

The project includes automated unit tests.

Run:

```bash
pytest
```

Current status:

```
15 Tests Passing ✅
```

---

# 📊 Logging

The application uses structured logging.

Example:

```
INFO | speech_service | Speech detected

INFO | agent_service | Planner selected weather tool

INFO | weather_service | Weather fetched successfully
```

---

# 🚀 Installation

Clone the repository

```bash
git clone <repository-url>
```

Create a virtual environment

```bash
python -m venv venv
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```
GEMINI_API_KEY=YOUR_KEY
OPENWEATHER_API_KEY=YOUR_KEY
```

Run

```bash
python voice_chat.py
```

---

# 📸 Demo

Example commands:

- Hello
- Open calculator
- Open Chrome
- Open Notepad
- What is the weather?
- Delhi

---

# 📈 Engineering Practices

This project follows:

- Clean Architecture
- Separation of Concerns
- Modular Services
- Plugin Architecture
- Registry Pattern
- Dependency Injection Principles
- Feature Branch Git Workflow
- Automated Testing
- Structured Logging

---

# 🔮 Future Roadmap (v2)

- Browser Automation
- Email Agent
- Calendar Integration
- File System Tools
- Long-Term Memory
- Docker Support
- CI/CD Pipeline
- Web Dashboard

---

# 👨‍💻 Developer

**Harshdeep Singh**

B.Tech Information Technology

AI Voice Agent Internship Project

Built as a production-style backend engineering project to strengthen software engineering fundamentals.