from agent.kubernetes_agent import KubernetesAgent
from tools.factory import create_tool_registry


class MockLLM:
    def generate(self, prompt):
        return "kubernetes_pods"



def test_unified_agent_response():

    registry = create_tool_registry()

    agent = KubernetesAgent(
        llm=MockLLM(),
        tool_registry=registry
    )


    response = agent.run(
        "Analyze Kubernetes cluster health"
    )


    assert "cluster_health" in response

    assert "remediation" in response

    assert "cluster_status" in response["cluster_health"]

    assert "recommended_actions" in response["remediation"]