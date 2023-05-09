import os

import aiofiles

from semantic_kernel.orchestration.sk_context import SKContext
from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter

class FileIOSkill:
    
    @sk_function(
        description="Read a file",
        name="readAsync",
        input_description="Path of the source file",
    )
    async def read_async(self, path: str) -> str:
        assert os.path.exists(path), f"File {path} does not exist"
        
        async with aiofiles.open(path, "r", encoding="UTF-8") as fp:
            content = await fp.read()
            return content

    @sk_function(
        description="Write a file",
        name="WriteAsync"
    )
    @sk_function_context_parameter(name="path", description="Destination path")
    @sk_function_context_parameter(name="content", description="File content")
    async def write_async(self, context: SKContext):
        has_path, path = context.variables.get("path")
        has_content, content = context.variables.get("content")        
        
        assert has_path, "Path is required"
        assert has_content, "Content is required"
        assert content is not None, "Content is required and should not be empty"
        assert path is not None, "Path is required and should not be empty"
        
        async with aiofiles.open(path, "w") as fp:
            await fp.write(content)