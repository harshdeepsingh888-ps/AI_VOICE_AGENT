import whisper

from app.utils.logger import setup_logger
from app.services.recorder import Recorder


logger = setup_logger("speech_service")

# Load Whisper model once when the application starts
logger.info("Loading Whisper model...")
model = whisper.load_model("base")
logger.info("Whisper model loaded successfully.")

recorder = Recorder()


def transcribe_audio(filename: str = "recording.wav") -> str:
    logger.info(f"Transcribing audio: {filename}")

    try:
        result = model.transcribe(
            filename,
            language="en",
        )

        text = result["text"].strip()

        logger.info(f"Transcription: {text}")

        return text

    except Exception as e:
        logger.exception("Speech transcription failed.")
        raise e


def listen() -> str:
    logger.info("Waiting for user speech...")

    recorder.wait_for_speech()

    logger.info("Speech detected.")

    return transcribe_audio()