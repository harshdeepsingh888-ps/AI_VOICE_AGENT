from app.tools.tool_manager import tool_manager


class ToolDispatcher:
    def execute(self, user_message: str):
        return tool_manager.execute(user_message)


tool_dispatcher = ToolDispatcher()