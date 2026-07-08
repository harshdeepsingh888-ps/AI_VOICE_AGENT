from app.services.speech_service import listen
from app.services.speech_normalizer import speech_normalizer
from app.services.agent_service import agent_service
from app.tools import (
    app_launcher,
    calculator_tool,
    weather_tool,
)
from app.utils.logger import setup_logger


logger = setup_logger("voice_chat")

logger.info("=" * 50)
logger.info("AI Voice Agent Started")
logger.info("Say 'exit' to quit.")
logger.info("=" * 50)

session_id = "voice_session"

while True:
    try:
        user_text = listen()

        logger.info(f"[Speech] User: {user_text}")

        clean_text = user_text.lower().strip()

        if not clean_text:
            logger.info("[System] No speech detected. Listening again.")
            continue

        if "exit" in clean_text or "quit" in clean_text or "stop" in clean_text:
            logger.info("[System] Goodbye!")
            break

        normalized_text = speech_normalizer.normalize(user_text)
        logger.info(f"[Normalizer] Normalized: {normalized_text}")

        response = agent_service.process(
            session_id=session_id,
            message=normalized_text,
        )

        logger.info(f"[Response] {response}")

    except KeyboardInterrupt:
        logger.info("[System] AI Voice Agent stopped.")
        break

    except Exception as e:
        logger.error(f"[Error] {e}")
        logger.info("[System] Continuing...")