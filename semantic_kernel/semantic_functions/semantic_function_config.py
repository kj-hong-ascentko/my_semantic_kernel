from dataclasses import dataclass
from typing import TYPE_CHECKING
from semantic_kernel.semantic_functions.semantic_function_config import PromptTemplateConfig
from semantic_kernel.semantic_functions.prompt_template import PromptTemplate
class ChatPromptTemplate:
    ...


@dataclass
class SemanticFunctionConfig:
    prompt_template_config: PromptTemplateConfig
    prompt_template: PromptTemplate

    @property
    def has_chat_prompt(self) -> bool:
        return isinstance(self.prompt_template, ChatPromptTemplate)