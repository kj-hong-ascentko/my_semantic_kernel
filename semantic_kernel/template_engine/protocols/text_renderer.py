from typing import Optional, Protocol, runtime_checkable

from semantic_kernel.orchestration.context_variables import ContextVariables

@runtime_checkable
class TextRenderer(Protocol):
    def render(self, variables: Optional[ContextVariables] = None) -> str:
        ...