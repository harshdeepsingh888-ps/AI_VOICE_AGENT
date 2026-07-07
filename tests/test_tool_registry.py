from app.tools.base_tool import BaseTool
from app.tools.tool_registry import ToolRegistry


class DummyTool(BaseTool):
    name = "dummy"
    description = "Dummy test tool."
    keywords = ["dummy"]

    def execute(self, *args, **kwargs):
        return "dummy executed"


def test_register_tool():
    registry = ToolRegistry()
    tool = DummyTool()

    registry.register(tool)

    assert registry.get_tool("dummy") == tool


def test_prevent_duplicate_registration():
    registry = ToolRegistry()
    tool = DummyTool()

    registry.register(tool)
    registry.register(tool)

    assert len(registry.get_all_tools()) == 1


def test_list_tool_names():
    registry = ToolRegistry()
    tool = DummyTool()

    registry.register(tool)

    assert registry.list_tool_names() == ["dummy"]


def test_find_matching_tool():
    registry = ToolRegistry()
    tool = DummyTool()

    registry.register(tool)

    assert registry.find_matching_tool("run dummy tool") == tool