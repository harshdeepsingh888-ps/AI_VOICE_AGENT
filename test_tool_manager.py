from app.tools.tool_manager import tool_manager
from app.tools.app_launcher import (
    open_notepad,
    open_calculator,
)

tool_manager.register_tool("notepad", open_notepad)
tool_manager.register_tool("calculator", open_calculator)

print(tool_manager.run_tool("notepad"))