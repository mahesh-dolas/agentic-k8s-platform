from agent.kubernetes_agent import KubernetesAgent
from tools.factory import create_tool_registry


class MockLLM:

    def generate(self, prompt):
        return "Kubernetes analysis plan"


def test_kubernetes_agent_tool_execution():

    # Create tool registry with Kubernetes tools
    registry = create_tool_registry()

    # Create Kubernetes agent
    agent = KubernetesAgent(
        MockLLM(),
        registry
    )

    # Execute Kubernetes health tool through the agent
    result = agent.execute_tool(
        "kubernetes_health",
        {}
    )

    assert result["status"] == "healthy"
    assert result["message"] == "Kubernetes cluster is healthy"