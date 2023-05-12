from semantic_kernel.kernel_extensions.import_skills import ImportSkills
from semantic_kernel.kernel_extensions.inline_definition import InlineDefinition
from semantic_kernel.kernel_extensions.memory_configuration import MemoryConfiguration


class KernelExtensions(
    ImportSkills,
    InlineDefinition,
    MemoryConfiguration,
):
    ...