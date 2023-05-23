from logging import Logger
from typing import TYPE_CHECKING, Dict, Literal, Optional, Tuple

from semantic_kernel.kernel_exception import KernelException

class FunctionsView:
    ...
class ReadOnlySkillCollection:
    ...

from semantic_kernel.skill_definition.skill_collection_base import SkillCollectionBase
from semantic_kernel.utils.null_logger import NullLogger
from semantic_kernel.utils.static_property import static_property

if TYPE_CHECKING:
    from semantic_kernel.orchestration.sk_function_base import SKFunctionBase
    from semantic_kernel.skill_definition.read_only_skill_collection_base import (
        ReadOnlySkillCollectionBase,
    )

