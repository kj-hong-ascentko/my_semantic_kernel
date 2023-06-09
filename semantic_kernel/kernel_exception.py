from enum import Enum
from typing import Optional

class KernelException(Exception):
    class ErrorCodes(Enum):
        # Unknown error.
        UnknownError = -1
        # Invalid function description.
        InvalidFunctionDescription = 0
        # Function overload not supported.
        FunctionOverloadNotSupported = 1
        # Function not available.
        FunctionNotAvailable = 2
        # Function type not supported.
        FunctionTypeNotSupported = 3
        # Invalid function type.
        InvalidFunctionType = 4
        # Invalid backend configuration.
        InvalidBackendConfiguration = 5
        # Backend not found.
        BackendNotFound = 6
        # Skill collection not set.
        SkillCollectionNotSet = 7
        # Ambiguous implementation.
        AmbiguousImplementation = 8

    _error_code: ErrorCodes
    
    def __init__(
        self,
        error_code: ErrorCodes,
        message: str,
        inner_exception: Optional[Exception] = None,
    ) -> None:
        super().__init__(error_code, message, inner_exception)
        self._error_code = error_code
    
    @property
    def error_code(self) -> ErrorCodes:
        return self._error_code