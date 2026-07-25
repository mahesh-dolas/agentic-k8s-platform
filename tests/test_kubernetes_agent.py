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

    assert response["status"] == "healthy"
    assert response["message"] == "Kubernetes cluster is healthy"