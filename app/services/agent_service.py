from app.services.llm_service import llm_service
from app.tools.tool_manager import tool_manager
from app.tools.tool_dispatcher import tool_dispatcher


class AgentService:
    def process(self, session_id: str, message: str):
        plan = llm_service.plan_tool_usage(message)

        if plan.error:
            print(f"[Agent] Planner failed: {plan.error}")

        if plan.use_tool and plan.tool_name:
            tool = tool_manager.registry.get_tool(plan.tool_name)

            if tool:
                user_message = plan.arguments.get("user_message", message)
                return tool.execute(user_message)

            print(f"[Agent] Invalid tool from planner: {plan.tool_name}")

        tool_response = tool_dispatcher.execute(message)

        if tool_response:
            return tool_response

        return llm_service.generate_response(
            session_id=session_id,
            message=message
        )


agent_service = AgentService()