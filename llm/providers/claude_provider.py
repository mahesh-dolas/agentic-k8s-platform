from llm.provider import LLMProvider


class ClaudeProvider(LLMProvider):

    def generate(self, prompt):

        return {
            "provider": "Anthropic Claude",
            "response": f"Claude response for: {prompt}"
        }