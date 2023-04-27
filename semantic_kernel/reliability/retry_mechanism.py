import abc
import logging
from typing import Awaitable, Callable, TypeVar

T = TypeVar("T")

class RetryMechanism(abc.ABC):
    @abc.abstractmethod
    async def execute_with_retry_async(
        self, action: Callable[[], Awaitable[T]], log: logging.Logger
    ) -> Awaitable[T]:
        pass