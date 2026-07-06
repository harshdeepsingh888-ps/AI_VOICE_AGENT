from typing import List

from app.tools.base_tool import BaseTool


class ToolRegistry:
    def __init__(self):
        self._tools: List[BaseTool] = []

    def register(self, tool: BaseTool) -> None:
        self._tools.append(tool)

    def get_all_tools(self) -> List[BaseTool]:
        return self._tools

    def find_matching_tool(self, user_message: str):
        for tool in self._tools:
            if tool.matches(user_message):
                return tool

        return None