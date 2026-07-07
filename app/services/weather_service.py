import os
import requests
from dotenv import load_dotenv

load_dotenv()


class WeatherService:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str):
        if not self.api_key:
            return {
                "success": False,
                "error": "OpenWeather API key is missing."
            }

        try:
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"
            }

            response = requests.get(self.base_url, params=params, timeout=10)
            data = response.json()

            if response.status_code != 200:
                return {
                    "success": False,
                    "error": data.get("message", "Unable to fetch weather.")
                }

            return {
                "success": True,
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "condition": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


weather_service = WeatherService()