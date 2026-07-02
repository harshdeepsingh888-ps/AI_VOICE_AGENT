import asyncio
import edge_tts
import pygame


class TTSService:
    def __init__(self):
        self.voice = "en-US-GuyNeural"

    async def text_to_speech(self, text):
        output_file = "response.mp3"

        communicate = edge_tts.Communicate(text, self.voice)
        await communicate.save(output_file)

        pygame.mixer.init()
        pygame.mixer.music.load(output_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)


tts_service = TTSService()