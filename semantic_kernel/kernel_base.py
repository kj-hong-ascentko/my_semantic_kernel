from abc import ABC, abstractmethod
from logging import Logger
from typing import Any, Dict, Optional
from semantic_kernel.kernel_config import KernelConfig
from semantic_kernel.memory.semantic_text_memory_base import SemanticTextMemoryBase
class KernelBase(ABC):
    @property
    @abstractmethod
    def config(self) -> KernelConfig:
        pass
    
    @property
    @abstractmethod
    def logger(self) -> Logger:
        pass
    
    @property
    @abstractmethod
    def memory(self) -> SemanticTextMemoryBase:
        pass
    
    @property
    @abstractmethod
    def prompt_template_engine(self) -> PromptTemplatingEngine:
        pass
    
    @property
    @abstractmethod
    def skills(self) -> ReadOnlySkillCollectionBase:
        pass
    
    @abstractmethod
    def register_semantic_function(
        self,
        skill_name: Optional[str],
        function_name: str,
        function_config: SemanticFunctionConfig,
    ) -> SKFunctionBase:
        pass

    @abstractmethod
    def import_skill(
        self, skill_instance: Any, skill_name: str = ""
    ) -> Dict[str, SKFunctionBase]:
        pass
    
    @abstractmethod
    def register_memory(self, memory: SemanticTextMemoryBase) -> None:
        pass

    @abstractmethod
    async def run_on_str_async(self, input_str: str, *args: Any) -> SKContext:
        pass
    
    @abstractmethod
    async def run_on_vars_async(
        self, input_vars: ContextVariables, *args: Any
    ) -> SKContext:
        pass
    
    @abstractmethod
    async def run_async(self, *args: Any) -> SKContext:
        pass
    
    @abstractmethod
    def func(self, skill_name: str, function_name: str) -> SKFunctionBase:
        pass

    @abstractmethod
    def create_new_context(self) -> SKContext:
        pass