from typing import List, Optional

from app.tools.base_tool import BaseTool


class ToolRegistry:
    def __init__(self):
        self._tools: List[BaseTool] = []

    def register(self, tool: BaseTool) -> None:
        """
        Register a tool if it has not already been registered.
        """
        if self.get_tool(tool.name):
            return

        self._tools.append(tool)

    def get_all_tools(self) -> List[BaseTool]:
        return self._tools

    def get_tool(self, name: str) -> Optional[BaseTool]:
        """
        Return a tool by its name.
        """
        for tool in self._tools:
            if tool.name == name:
                return tool

        return None

    def list_tool_names(self) -> List[str]:
        """
        Return the names of all registered tools.
        """
        return [tool.name for tool in self._tools]

    def find_matching_tool(self, user_message: str) -> Optional[BaseTool]:
        """
        Return the first tool that matches the user message.
        """
        for tool in self._tools:
            if tool.matches(user_message):
                return tool

        return None