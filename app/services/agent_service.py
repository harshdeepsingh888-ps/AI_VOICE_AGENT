from app.services.llm_service import llm_service
from app.tools.tool_manager import tool_manager
from app.tools.tool_dispatcher import tool_dispatcher


class AgentService:
    def __init__(self):
        self.pending_requests = {}

    def process(self, session_id: str, message: str):
        pending_tool = self.pending_requests.get(session_id)

        if pending_tool == "weather":
            weather_tool = tool_manager.registry.get_tool("weather")

            if weather_tool:
                result = weather_tool.execute(f"weather in {message}")

                if "Sorry, I could not fetch the weather" not in result:
                    self.pending_requests.pop(session_id, None)

                return result

        plan = llm_service.plan_tool_usage(message)

        if plan.error:
            print(f"[Agent] Planner failed: {plan.error}")

        if plan.use_tool and plan.tool_name:
            tool = tool_manager.registry.get_tool(plan.tool_name)

            if tool:
                user_message = plan.arguments.get("user_message", message)
                result = tool.execute(user_message)

                if result == "Please tell me the city name.":
                    self.pending_requests[session_id] = plan.tool_name

                return result

            print(f"[Agent] Invalid tool from planner: {plan.tool_name}")

        tool_response = tool_dispatcher.execute(message)

        if tool_response:
            if tool_response == "Please tell me the city name.":
                self.pending_requests[session_id] = "weather"

            return tool_response

        return llm_service.generate_response(
            session_id=session_id,
            message=message,
        )


agent_service = AgentService()