from app.tools import app_launcher
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

        calculator_keywords = [
            "calculator",
            "calculate",
            "calc",
        ]

        chrome_keywords = [
            "chrome",
            "google chrome",
            "browser",
        ]

        if any(keyword in message for keyword in notepad_keywords):
            return tool_manager.run_tool("notepad")

        if any(keyword in message for keyword in calculator_keywords):
            return tool_manager.run_tool("calculator")
        
        if any(keyword in message for keyword in chrome_keywords):
            return tool_manager.run_tool("chrome")

        return None


tool_dispatcher = ToolDispatcher()