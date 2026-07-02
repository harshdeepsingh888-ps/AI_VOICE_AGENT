from fastapi import FastAPI
from app.core.config import settings
from app.api.chat import router as chat_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

# Register Chat API
app.include_router(chat_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Voice Agent 🚀",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }