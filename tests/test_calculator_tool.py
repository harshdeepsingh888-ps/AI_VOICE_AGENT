from app.tools import calculator_tool
from app.tools.tool_dispatcher import tool_dispatcher


def test_addition():
    result = tool_dispatcher.execute("what is 5 plus 3")
    assert result == "The answer is 8."


def test_subtraction():
    result = tool_dispatcher.execute("10 minus 4")
    assert result == "The answer is 6."


def test_multiplication():
    result = tool_dispatcher.execute("7 times 8")
    assert result == "The answer is 56."


def test_division():
    result = tool_dispatcher.execute("20 divided by 5")
    assert result == "The answer is 4.0."