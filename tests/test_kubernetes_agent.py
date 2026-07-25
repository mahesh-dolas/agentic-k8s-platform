from agent.kubernetes_agent import KubernetesAgent
from tools.factory import create_tool_registry


class MockLLM:

    def generate(self, prompt):
        return "kubernetes_health"


def test_kubernetes_agent():

    registry = create_tool_registry()

    agent = KubernetesAgent(
        MockLLM(),
        registry
    )

    response = agent.run(
        "Check Kubernetes cluster health"
    )

    assert len(response) == 1

    assert response[0]["tool"] == "kubernetes_health"

    assert response[0]["result"]["status"] == "healthy"