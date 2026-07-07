from app.tools.base_tool import BaseTool
from app.tools.tool_manager import ToolManager


class DummyTool(BaseTool):
    name = "dummy"
    description = "Dummy Tool"
    keywords = ["dummy"]

    def execute(self, user_message: str):
        return "dummy executed"


def test_execute_matching_tool():
    manager = ToolManager()
    manager.register_tool(DummyTool())

    result = manager.execute("run dummy")

    assert result == "dummy executed"


def test_execute_unknown_tool():
    manager = ToolManager()

    result = manager.execute("something else")

    assert result is None