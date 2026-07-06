import re

from app.tools.tool_manager import tool_manager


def calculate_expression(expression: str):
    try:
        expression = expression.replace("?", "").strip()

        if not re.match(r"^[0-9+\-*/().\s]+$", expression):
            return "Invalid mathematical expression."

        result = eval(expression)

        return f"The answer is {result}."

    except Exception:
        return "Sorry, I could not calculate that."


tool_manager.register_tool("calculator_expression", calculate_expression)