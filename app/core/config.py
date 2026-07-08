import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    # ==========================
    # Application
    # ==========================
    APP_NAME = os.getenv("APP_NAME", "AI Voice Agent")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

    # ==========================
    # Gemini
    # ==========================
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    # ==========================
    # Weather
    # ==========================
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

    # ==========================
    # Agent
    # ==========================
    DEFAULT_SESSION_ID = os.getenv(
        "DEFAULT_SESSION_ID",
        "voice_session",
    )

    # ==========================
    # Logging
    # ==========================
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()