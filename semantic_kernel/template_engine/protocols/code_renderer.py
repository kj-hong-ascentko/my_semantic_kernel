
from typing import Optional, Protocol, runtime_checkable
from semantic_kernel.orchestration.sk_context import SKContext

@runtime_checkable
class CodeRenderer(Protocol):
    def render_code_async(self, context: SKContext) -> str:
        ...