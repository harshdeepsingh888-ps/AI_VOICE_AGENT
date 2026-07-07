import re

from app.tools.base_tool import BaseTool
from app.tools.tool_manager import tool_manager
from app.services.weather_service import weather_service


class WeatherTool(BaseTool):
    name = "weather"
    description = "Gets current weather for a city."

    keywords = [
        "weather",
        "temperature",
        "forecast",
    ]

    def matches(self, user_message: str) -> bool:
        message = user_message.lower()
        return any(keyword in message for keyword in self.keywords)

    def execute(self, user_message: str):
        city = self._extract_city(user_message)

        if not city:
            return "Please tell me the city name."

        weather = weather_service.get_weather(city)

        if not weather["success"]:
            return f"Sorry, I could not fetch the weather. {weather['error']}"

        return (
            f"The current weather in {weather['city']} is "
            f"{weather['temperature']} degrees Celsius with "
            f"{weather['condition']}. It feels like "
            f"{weather['feels_like']} degrees Celsius, and humidity is "
            f"{weather['humidity']} percent."
        )

    def _extract_city(self, message: str) -> str:
        message = message.lower().strip()

        patterns = [
    r"weather in ([a-zA-Z\s]+)",
    r"temperature in ([a-zA-Z\s]+)",
    r"forecast in ([a-zA-Z\s]+)",
    r"weather of ([a-zA-Z\s]+)",
    r"weather for ([a-zA-Z\s]+)",
    r"weather at ([a-zA-Z\s]+)",
]

        for pattern in patterns:
            match = re.search(pattern, message)
            if match:
                return match.group(1).strip()

        return ""


tool_manager.register_tool(WeatherTool())