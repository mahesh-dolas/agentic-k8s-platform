from abc import ABC, abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    def generate(self, prompt: str):
        """
        Generate response from LLM provider
        """
        pass