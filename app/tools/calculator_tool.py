import re

from app.tools.base_tool import BaseTool
from app.tools.tool_manager import tool_manager


class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Performs basic mathematical calculations."

    keywords = [
        "calculate",
        "what is",
        "what's",
        "plus",
        "minus",
        "times",
        "multiplied by",
        "divided by",
    ]

    def matches(self, user_message: str) -> bool:
        message = user_message.lower()

        has_number = bool(re.search(r"\d", message))
        has_operator = any(
            operator in message
            for operator in [
                "plus",
                "minus",
                "times",
                "multiplied by",
                "divided by",
            ]
        )

        return has_number and has_operator

    def execute(self, user_message: str):
        expression = self._extract_expression(user_message)

        try:
            if not re.fullmatch(r"[0-9+\-*/().\s]+", expression):
                return "Invalid mathematical expression."

            result = eval(expression)
            return f"The answer is {result}."

        except Exception:
            return "Sorry, I could not calculate that."

    def _extract_expression(self, message: str) -> str:
        expression = message.lower()

        expression = expression.replace("multiplied by", "*")
        expression = expression.replace("divided by", "/")
        expression = expression.replace("times", "*")
        expression = expression.replace("plus", "+")
        expression = expression.replace("minus", "-")

        # Try to extract a clean mathematical expression first
        match = re.search(
            r"(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)",
            expression,
        )

        if match:
            return match.group(0)

        # Fallback cleanup
        expression = re.sub(r"[^0-9+\-*/().\s]", " ", expression)
        expression = re.sub(r"\s+", " ", expression).strip()

        return expression


tool_manager.register_tool(CalculatorTool())