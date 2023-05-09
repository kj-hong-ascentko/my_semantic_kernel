import json

import aiohttp

from semantic_kernel.core_skills.skill import SKContext
from semantic_kernel.skill_definition import sk_function, sk_function_context_parameter

class HttpSkill:
    
    @sk_function(description="Makes a GET request to a uri", name="getAsync")
    async def get_async(self, url: str) -> str:
        if not url:
            raise ValueError("url cannot be `None` or empty")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, raise_for_status=True) as response:
                return await response.text()
    
    @sk_function(description="Makes a POST request to a uri", name="postAsync")
    @sk_function_context_parameter(name="body", description="The body of the request")
    async def post_async(self, url: str, context: SKContext) -> str:
        if not url:
            raise ValueError("url cannot be `None` or empty")        

        _, body = context.variables.get("body")
        headers = {"Content-Type": "application/json"}
        data = json.dumps(body)
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url, headers=headers, data=data, raise_for_status=True
            ) as response:
                return await response.text()        
    
    @sk_function(description="Makes a PUT request to a uri", name="putAsync")
    @sk_function_context_parameter(name="body", description="The body of the request")
    async def put_async(self, url: str, context: SKContext) -> str:
        if not url:
            raise ValueError("url cannot be `None` or empty")                

        _, body = context.variables.get("body")

        headers = {"Content-Type": "application/json"}
        data = json.dumps(body)        
        async with aiohttp.ClientSession() as session:
            async with session.put(
                url, headers=headers, data=data, raise_for_status=True
            ) as response:
                return await response.text()
    
    @sk_function(description="Makes a DELETE request to a uri", name="deleteAsync")
    async def delete_async(self, url: str) -> str:
        if not url:
            raise ValueError("url cannot be `None` or empty")                
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, raise_for_status=True) as response:
                return await response.text()            
            

                