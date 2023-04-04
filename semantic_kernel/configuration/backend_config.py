from typing import Optional
from semantic_kernel.configuration.backend_types import BackendType
class BackendConfig:
    backend_type: BackendType = BackendType.Unknown
    open_ai: Optional[OpenAIConfig] = None
    
    