import subprocess

from app.tools.tool_manager import tool_manager


def open_notepad():
    subprocess.Popen("notepad.exe")
    return "Notepad opened successfully."


def open_calculator():
    subprocess.Popen("calc.exe")
    return "Calculator opened successfully."


# Register tools
tool_manager.register_tool("notepad", open_notepad)
tool_manager.register_tool("calculator", open_calculator)