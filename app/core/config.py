from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "AI Voice Agent")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

settings = Settings()