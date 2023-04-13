from logging import Logger
from typing import TYPE_CHECKING, List, Optional

from semantic_kernel.semantic_functions.prompt_template_base import PromptTemplateBase
from semantic_kernel.semantic_functions.prompt_template_config import PromptTemplateConfig

class ParameterView:
    ...

class BlockTypes:
    ...

class VarBlock:
    ...

class PromptTemplatingEngine:
    ...

from semantic_kernel.utils.null_logger import NullLogger

class SKContext:
    ...    

class PromptTemplate(PromptTemplateBase):
    _template: str
    _template_engine: PromptTemplatingEngine
    prompt_config: PromptTemplateConfig
    _log: Optional[Logger] = None,
    
    def __init__(
        self,
        template: str,
        template_engine: PromptTemplatingEngine,
        prompt_config: PromptTemplateConfig,
        log: Optional[Logger] = None,
    ) -> None:
        self._template = template
        self._template_engine = template_engine
        self._prompt_config = prompt_config
        self._log = log if log is not None else NullLogger()

            
    
    def get_parameters(self) -> List["ParameterView"]:
        seen = set()
        result = []
        for param in self._prompt_config.input.parameters:
            if param is None:
                continue

            result.append(
                ParameterView(param.name, param.description, param.default_value)
            )

            seen.add(param.name)
        
        blocks = self._template_engine.extract_blocks(self._template)
        for block in blocks:
            if block.type != BlockTypes.VARIABLE:
                continue
            if block is None:
                continue
            
            var_block: VarBlock = block
            if var_block.name in seen:
                continue
            
            result.append(ParameterView(var_block.name, "", ""))
            seen.add(var_block.name)
        
        return result
            
    async def render_async(self, context: "SKContext") -> str:
        return await self._template_engine.render_async(self._template, context)