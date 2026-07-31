from llm.gateway import LLMGateway
from llm.providers.openai_provider import OpenAIProvider


def test_llm_gateway():

    gateway = LLMGateway(
        OpenAIProvider()
    )

    response = gateway.ask(
        "Explain Kubernetes pods"
    )

    assert response["provider"] == "OpenAI"