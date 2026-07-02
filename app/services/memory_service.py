class MemoryService:

    def __init__(self):
        self.conversations = {}

    def get_history(self, session_id: str):
        if session_id not in self.conversations:
            self.conversations[session_id] = []
        return self.conversations[session_id]

    def add_message(self, session_id: str, role: str, content: str):
        history = self.get_history(session_id)
        history.append({
            "role": role,
            "content": content
        })


memory_service = MemoryService()