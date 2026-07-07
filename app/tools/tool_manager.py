import time

from app.tools.base_tool import BaseTool
from app.tools.tool_registry import ToolRegistry


class ToolManager:
    def __init__(self):
        self.registry = ToolRegistry()

    def register_tool(self, tool: BaseTool) -> None:
        self.registry.register(tool)

    def execute(self, user_message: str):
        tool = self.registry.find_matching_tool(user_message)

        if tool is None:
            return None

        start_time = time.perf_counter()

        result = tool.execute(user_message)

        elapsed_ms = (time.perf_counter() - start_time) * 1000

        print(
            f"[Tool] {tool.name} | "
            f"Input: {user_message} | "
            f"Time: {elapsed_ms:.2f} ms"
        )

        return result


tool_manager = ToolManager()