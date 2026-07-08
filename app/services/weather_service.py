import requests

from app.core.config import settings
from app.utils.logger import setup_logger


logger = setup_logger("weather_service")


class WeatherService:
    def __init__(self):
        self.api_key = settings.OPENWEATHER_API_KEY
        self.base_url = (
            "https://api.openweathermap.org/data/2.5/weather"
        )

    def get_weather(self, city: str):
        logger.info(f"Fetching weather for '{city}'")

        if not self.api_key:
            logger.error("OpenWeather API key is missing.")

            return {
                "success": False,
                "error": "OpenWeather API key is missing.",
            }

        try:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric",
            }

            response = requests.get(
                self.base_url,
                params=params,
                timeout=10,
            )

            data = response.json()

            if response.status_code != 200:
                logger.warning(
                    f"Weather lookup failed for '{city}': "
                    f"{data.get('message')}"
                )

                return {
                    "success": False,
                    "error": data.get(
                        "message",
                        "Unable to fetch weather.",
                    ),
                }

            logger.info(f"Weather fetched successfully for '{city}'")

            return {
                "success": True,
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "condition": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
            }

        except requests.RequestException as e:
            logger.exception("Weather API request failed")

            return {
                "success": False,
                "error": str(e),
            }

        except Exception as e:
            logger.exception("Unexpected weather service error")

            return {
                "success": False,
                "error": str(e),
            }


weather_service = WeatherService()