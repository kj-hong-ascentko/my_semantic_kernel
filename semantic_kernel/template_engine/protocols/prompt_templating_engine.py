from typing import List, Optional, Protocol

class ContextVariables:
    ...

class SKContext:
    ...
class Block:
    ...

class PromptTemplatingEngine(Protocol):
    def extract_blocks(
        self, template_text: Optional[str] = None, validate: bool = True
        ) -> List[Block]:
        ...

    async def render_async(self, template_text: str, context: SKContext) -> str:
        ...
    
    async def render_blocks_async(self, blocks: List[Block], context: SKContext) -> str:
        ...    
    
    def render_variables(
        self, blocks: List[Block], variables: Optional[ContextVariables] = None
        ) -> List[Block]:
        ...
    
    async def render_code_async(self, code: str, context: SKContext) -> str:
        ...