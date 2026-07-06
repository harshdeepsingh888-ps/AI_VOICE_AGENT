from app.tools import app_launcher
from app.tools import calculator_tool
from app.tools.tool_manager import tool_manager


class ToolDispatcher:

    def execute(self, user_message: str):
        message = user_message.lower()

        notepad_keywords = [
            "notepad",
            "note pad",
            "not bad",
            "north pad",
            "north bad",
            "open pad",
        ]

        chrome_keywords = [
            "chrome",
            "google chrome",
            "browser",
        ]

        if any(keyword in message for keyword in notepad_keywords):
            return tool_manager.run_tool("notepad")

        if any(keyword in message for keyword in chrome_keywords):
            return tool_manager.run_tool("chrome")

        if (
    "calculate" in message
    or "what is" in message
    or "multiplied by" in message
    or "times" in message
    or "plus" in message
    or "minus" in message
    or "divided by" in message
):
            expression = (
                message.replace("calculate", "")
                .replace("what is", "")
                .replace("multiplied by", "*")
                .replace("times", "*")
                .replace("plus", "+")
                .replace("minus", "-")
                .replace("divided by", "/")
                .strip()
            )

            return tool_manager.run_tool("calculator_expression", expression)

        return None


tool_dispatcher = ToolDispatcher()