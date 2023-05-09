from typing import Optional

def sk_function_context_parameter(
    *, name: str, description: str, default_value: Optional[str] = None
):
    def decorator(func):
        if not hasattr(func, "__sk_function_context_parameters__"):
            func.__sk_function_context_parameters__ = []
        
        func.__sk_function_context_parameters__.append(
            {
                "name": name,
                "description": description,
                "default_value": default_value,  
            }
        )
        return func
    return decorator