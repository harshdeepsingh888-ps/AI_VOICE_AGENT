from abc import ABC, abstractmethod
from typing import List


class BaseTool(ABC):
    name: str = ""
    description: str = ""
    keywords: List[str] = []
    version: str = "1.0.0"
    enabled: bool = True

    def matches(self, user_message: str) -> bool:
        if not self.enabled:
            return False

        if not user_message:
            return False

        message = user_message.lower()
        return any(keyword.lower() in message for keyword in self.keywords)

    def get_metadata(self) -> dict:
        return {
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "enabled": self.enabled,
            "keywords": self.keywords,
        }

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass