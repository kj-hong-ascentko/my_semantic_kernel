from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    ...

class SKContext:
    ...

class ParameterView:
    ...

class PromptTemplateBase(ABC):
    @abstractmethod
    def get_parameters(self) -> List["ParameterView"]:
        pass
    
    @abstractmethod
    async def render_async(self, context: "SKContext") -> str:
        pass
    