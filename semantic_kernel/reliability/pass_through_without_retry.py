import logging
from typing import Awaitable, Callable, TypeVar

from semantic_kernel.reliability.retry_mechanism import RetryMechanism

T = TypeVar("T")

class PassThroughWithoutRetry(RetryMechanism):
    async def execute_with_retry_async(
        self, action: Callable[[], Awaitable[T]], log: logging.Logger
    ) -> Awaitable[T]:
        try:
            await action()
        except Exception as e:
            log.warning(e, "Error executing action, not retrying")
            raise