from semantic_kernel.skill_definition import sk_function

class TextSkill:
    @sk_function(description="Trim whitespace from the start and end of a string.")
    def trim(self, text: str) -> str:
        return text.strip()

    @sk_function(description="Trim whitespace from the start of a string.")
    def trim_start(self, text: str) -> str:
        return text.lstrip()

    @sk_function(description="Trim whitespace from the end of a string.")
    def trim_end(self, text: str) -> str:
        return text.rstrip()

    @sk_function(description="Convert a string to uppercase.")
    def uppercase(self, text: str) -> str:
        return text.upper()
    
    @sk_function(description="Convert a string to lowercase.")
    def lowercase(self, text: str) -> str:
        return text.lower()