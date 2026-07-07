import subprocess

from app.tools.base_tool import BaseTool
from app.tools.tool_manager import tool_manager


class NotepadTool(BaseTool):
    name = "notepad"
    description = "Opens Windows Notepad."

    keywords = [
        "notepad",
        "note pad",
        "not bad",
        "north pad",
        "north bad",
        "open pad",
    ]

    def execute(self, user_message: str):
        subprocess.Popen("notepad.exe")
        return "Notepad opened successfully."


class ChromeTool(BaseTool):
    name = "chrome"
    description = "Opens Google Chrome."

    keywords = [
        "chrome",
        "google chrome",
        "browser",
    ]

    def execute(self, user_message: str):
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        return "Chrome opened successfully."


class WindowsCalculatorTool(BaseTool):
    name = "windows_calculator"
    description = "Opens the Windows Calculator application."

    keywords = [
        "open calculator",
        "launch calculator",
        "calculator app",
    ]

    def execute(self, user_message: str):
        subprocess.Popen("calc.exe")
        return "Calculator opened successfully."


tool_manager.register_tool(NotepadTool())
tool_manager.register_tool(ChromeTool())
tool_manager.register_tool(WindowsCalculatorTool())