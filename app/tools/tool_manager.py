class ToolManager:

    def __init__(self):
        self.tools = {}

    def register_tool(self, name, function):
        self.tools[name] = function

    def run_tool(self, name, *args, **kwargs):
        if name not in self.tools:
            return f"Tool '{name}' not found."

        return self.tools[name](*args, **kwargs)


tool_manager = ToolManager()