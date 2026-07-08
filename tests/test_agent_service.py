from unittest.mock import patch

from app.schemas.tool_plan import ToolPlan
from app.services.agent_service import AgentService


def test_agent_uses_valid_planned_tool():
    agent = AgentService()

    plan = ToolPlan(
        use_tool=True,
        tool_name="calculator",
        arguments={"user_message": "what is 5 plus 3"},
    )

    with patch("app.services.agent_service.llm_service.plan_tool_usage", return_value=plan):
        result = agent.process("test_session", "what is 5 plus 3")

    assert result == "The answer is 8."


def test_agent_falls_back_when_planner_fails():
    agent = AgentService()

    plan = ToolPlan(
        use_tool=False,
        error="Planner failed",
    )

    with patch("app.services.agent_service.llm_service.plan_tool_usage", return_value=plan):
        result = agent.process("test_session", "what is 5 plus 3")

    assert result == "The answer is 8."