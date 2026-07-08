from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class ToolPlan:
    use_tool: bool
    tool_name: Optional[str] = None
    arguments: Dict = field(default_factory=dict)
    error: Optional[str] = None