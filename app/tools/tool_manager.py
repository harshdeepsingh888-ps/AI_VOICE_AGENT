from app.tools.tool_registry import ToolRegistry
from app.tools.base_tool import BaseTool


class ToolManager:
    def __init__(self):
        self.registry = ToolRegistry()

    def register_tool(self, tool: BaseTool) -> None:
        self.registry.register(tool)

    def execute(self, user_message: str):
        tool = self.registry.find_matching_tool(user_message)

        if tool is None:
            return None

        return tool.execute(user_message)


tool_manager = ToolManager()