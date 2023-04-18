from logging import Logger
from typing import Any, Literal, Optional, Tuple, Union

from semantic_kernel.kernel_exception import KernelException
from semantic_kernel.memory.semantic_text_memory_base import SemanticTextMemoryBase
from semantic_kernel.orchestration.context_variables import ContextVariables
from semantic_kernel.skill_definition.read_only_skill_collection_base import ReadOnlySkillCollectionBase

class SKContext:
    _error_occurred: bool = False
    _last_exception: Optional[Exception] = None
    _last_error_description: str = ""
    _logger: Logger
    _memory: SemanticTextMemoryBase
    _skill_collection: ReadOnlySkillCollectionBase
    _variables: ContextVariables
    
    def __init__(
        self,
        variables: ContextVariables,
        memory: SemanticTextMemoryBase,
        skill_collection: ReadOnlySkillCollectionBase,
        logger: Logger,        
    ) -> None:
        self._variables = variables
        self._memory = memory
        self._skill_collection = skill_collection
        self._logger = logger
    
    def fail(self, error_description: str, exception: Optional[Exception] = None):
        self._error_occurred = True
        self._last_error_description = error_description
        self._last_exception = exception

    @property
    def result(self) -> str:
        return str(self._variables)
    
    @property
    def error_occurred(self) -> bool:
        return self._error_occurred
    
    @property
    def last_error_description(self) -> str:
        return self._last_error_description    
    
    @property
    def last_exception(self) -> Optional[Exception]:
        return self._last_exception

    @property
    def variables(self) -> ContextVariables:
        return self._variables
    
    @property
    def memory(self) -> SemanticTextMemoryBase:
        return self._memory
    
    @property
    def skills(self) -> ReadOnlySkillCollectionBase:
        return self._skill_collection

    @skills.setter
    def skills(self, value: ReadOnlySkillCollectionBase):
        self._skill_collection = value
    
    @property
    def log(self) -> Logger:
        return self._logger    
    
    def __setitem__(self, key: str, value: Any):
        self._variables[key] = value

    def __getitem__(self, key: str) -> Any:
        return self._variables[key]
    
    def func(self, skill_name: str, function_name: str):
        if self._skill_collection is None:
            raise ValueError("The skill collection hasn't been set")
        assert self._skill_collection is not None  # for type checker
        
        if self._skill_collection.has_native_function(skill_name, function_name):
            return self._skill_collection.get_native_function(skill_name, function_name)

        return self._skill_collection.get_semantic_function(skill_name, function_name)

    def __str__(self) -> str:
        if self._error_occurred:
            return f"Error: {self._last_error_description}"

        return self.result        

    def throw_if_skill_collection_not_set(self) -> None:
        if self._skill_collection is None:            
            raise KernelException(
                KernelException.ErrorCodes.SkillCollectionNotSet,
                "Skill collection not found in the context",
            )

    def is_function_registered(
        self, skill_name: str, function_name: str
    ) -> Union[Tuple[Literal[True], Any], Tuple[Literal[False], None]]:
        self.throw_if_skill_collection_not_set()
        assert self._skill_collection is not None  # for type checker        

        if self._skill_collection.has_native_function(skill_name, function_name):
            the_func = self._skill_collection.get_native_function(
                skill_name, function_name
            )
            return True, the_func

        if self._skill_collection.has_native_function(None, function_name):
            the_func = self._skill_collection.get_native_function(None, function_name)
            return True, the_func

        if self._skill_collection.has_semantic_function(skill_name, function_name):
            the_func = self._skill_collection.has_semantic_function(skill_name, function_name)
            return True, the_func
    
        return False, None
