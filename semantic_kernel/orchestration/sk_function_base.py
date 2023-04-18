from abc import ABC, abstractmethod
from logging import Logger
from typing import TYPE_CHECKING, Callable, Optional

class CompleteRequestSettings:
    ...
class TextCompletionClientBase:
    ...

from semantic_kernel.memory.semantic_text_memory_base import SemanticTextMemoryBase

from semantic_kernel.orchestration.context_variables import ContextVariables
from semantic_kernel.orchestration.sk_context import SKContext

class FunctionView:
    ...

if TYPE_CHECKING:
    from semantic_kernel.skill_definition.read_only_skill_collection_base import (
        ReadOnlySkillCollectionBase,
    )

class SKFuntionBase(ABC):
    FUNCTION_PARAM_NAME_REGEX = r"^[0-9A-Za-z_]*$"
    FUNCTION_NAME_REGEX = r"^[0-9A-Za-z_]*$"
    SKILL_NAME_REGEX = r"^[0-9A-Za-z_]*$"
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @property
    @abstractmethod
    def skill_name(self) -> str:
        pass

    @property
    @abstractmethod
    def is_semantic(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_native(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def request_settings(self) -> CompleteRequestSettings:
        pass

    @abstractmethod
    def describe(self) -> FunctionView:
        pass
    
    @abstractmethod
    def invoke(
        self,
        input: Optional[str] = None,
        context: Optional[SKContext] = None,
        settings: Optional[CompleteRequestSettings] = None,
        log: Optional[Logger] = None
    ) -> SKContext:
        pass

    @abstractmethod
    async def invoke_async(
        self,
        input: Optional[str] = None,
        context: Optional[SKContext] = None,
        settings: Optional[CompleteRequestSettings] = None,
        log: Optional[Logger] = None
    ) -> SKContext:
        pass
    
    @abstractmethod
    def invoke_with_vars(
        self,
        input: ContextVariables,
        memory: Optional[SemanticTextMemoryBase],
        log: Optional[Logger] = None
    ) -> SKContext:
        pass
    
    @abstractmethod
    def invoke_with_vars_async(
        self,
        input: ContextVariables,
        memory: Optional[SemanticTextMemoryBase],
        log: Optional[Logger] = None
    ) -> SKContext:
        pass

    @abstractmethod
    def set_default_skill_collection(self, skills: "ReadOnlySkillCollectionBase") -> "SKFuntionBase":
        pass

    @abstractmethod
    def set_ai_backend(
        self, backend: Callable[[], TextCompletionClientBase]
    ) -> "SKFuntionBase":
        pass
    
    @abstractmethod
    def set_ai_configurations(
        self, configurations: CompleteRequestSettings
    ) -> "SKFuntionBase":
        pass