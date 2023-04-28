import asyncio
import threading
from enum import Enum
from logging import Logger
from typing import Any, Callable, List, Optional, cast

from semantic_kernel.connectors.ai.chat_completion_client_base import (
    ChatCompletionClientBase,
)
from semantic_kernel.connectors.ai.chat_request_settings import ChatRequestSettings
from semantic_kernel.connectors.ai.complete_request_settings import (
    CompleteRequestSettings,
)
from semantic_kernel.connectors.ai.text_completion_client_base import (
    TextCompletionClientBase,
)
from semantic_kernel.kernel_exception import KernelException
class NullMemory:
    ...

from semantic_kernel.memory.semantic_text_memory_base import SemanticTextMemoryBase
from semantic_kernel.orchestration.context_variables import ContextVariables

class DelegateHandlers:
    ...
class DelegateInference:
    ...
class DelegateTypes:
    ...

from semantic_kernel.orchestration.sk_context import SKContext
from semantic_kernel.orchestration.sk_function_base import SKFunctionBase
from semantic_kernel.semantic_functions.chat_prompt_template import ChatPromptTemplate
from semantic_kernel.semantic_functions.semantic_function_config import (
    SemanticFunctionConfig,
)
from semantic_kernel.skill_definition.function_view import FunctionView
from semantic_kernel.skill_definition.parameter_view import ParameterView
from semantic_kernel.skill_definition.read_only_skill_collection_base import (
    ReadOnlySkillCollectionBase,
)
from semantic_kernel.utils.null_logger import NullLogger

class SKFunction(SKFunctionBase):
    _parameter: List[ParameterView]
    _delegate_type: DelegateTypes
    _function: Callable[..., Any]
    _skill_collection: Optional[ReadOnlySkillCollectionBase]
    _log: Logger
    _ai_backend: Optional[TextCompletionClientBase]
    _ai_request_settings: CompleteRequestSettings
    _chat_backend: Optional[ChatCompletionClientBase]
    _chat_request_settings: ChatRequestSettings
    
    @staticmethod
    def from_native_method(method, skill_name="",log=None) -> "SKFunction":
        if method is None:
            raise ValueError("Method cannot be `None`")
        
        assert method.__sk_function__ is not None, "Method is not a SK function"
        assert method.__sk_function_name__ is not None, "Method name is empty"
        
        parameters = []
        if hasattr(method, "__sk_function_context_parameters__"):
            for param in method.__sk_function_context_parameters__:
                assert "name" in param, "Parameter name is empty"
                assert "description" in param, "Parameter description is empty"
                assert "default_value" in param, "Parameter default value is empty"

                parameters.append(
                    ParameterView(
                        param["name"], param["description"], param["default_value"]
                    )
                )
        