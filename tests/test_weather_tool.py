from unittest.mock import patch

from app.tools import weather_tool
from app.tools.tool_dispatcher import tool_dispatcher


def test_weather_tool_success():
    fake_weather = {
        "success": True,
        "city": "Delhi",
        "temperature": 30,
        "feels_like": 32,
        "condition": "clear sky",
        "humidity": 40,
    }

    with patch(
        "app.tools.weather_tool.weather_service.get_weather",
        return_value=fake_weather,
    ):
        result = tool_dispatcher.execute("weather in Delhi")

    assert "The current weather in Delhi is 30 degrees Celsius" in result
    assert "clear sky" in result
    assert "humidity is 40 percent" in result


def test_weather_tool_missing_city():
    result = tool_dispatcher.execute("weather")
    assert result == "Please tell me the city name."