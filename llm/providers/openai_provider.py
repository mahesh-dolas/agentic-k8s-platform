from llm.provider import LLMProvider


class OpenAIProvider(LLMProvider):

    def generate(self, prompt):

        return {
            "provider": "OpenAI",
            "response": f"Generated response for: {prompt}"
        }