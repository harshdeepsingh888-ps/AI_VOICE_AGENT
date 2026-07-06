from abc import ABC, abstractmethod
from typing import List


class BaseTool(ABC):
    name: str = ""
    description: str = ""
    keywords: List[str] = []

    def matches(self, user_message: str) -> bool:
        if not user_message:
            return False

        message = user_message.lower()
        return any(keyword.lower() in message for keyword in self.keywords)

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass