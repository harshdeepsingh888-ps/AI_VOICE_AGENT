import asyncio

import edge_tts
import pygame

from app.utils.logger import setup_logger


logger = setup_logger("tts_service")


class TTSService:
    def __init__(self):
        self.voice = "en-US-GuyNeural"

        logger.info("Initializing pygame mixer...")
        pygame.mixer.init()
        logger.info("TTS service initialized.")

    async def text_to_speech(self, text: str):
        output_file = "response.mp3"

        logger.info("Generating speech...")

        try:
            communicate = edge_tts.Communicate(
                text=text,
                voice=self.voice,
            )

            await communicate.save(output_file)

            logger.info("Speech generated successfully.")

            pygame.mixer.music.load(output_file)
            pygame.mixer.music.play()

            logger.info("Playing audio response...")

            while pygame.mixer.music.get_busy():
                await asyncio.sleep(0.1)

            pygame.mixer.music.unload()

            logger.info("Audio playback completed.")

        except Exception:
            logger.exception("TTS generation failed.")
            raise


tts_service = TTSService()