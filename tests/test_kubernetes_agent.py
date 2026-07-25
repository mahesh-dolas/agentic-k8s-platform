from agent.kubernetes_agent import KubernetesAgent


class MockLLM:

    def generate(self, prompt):
        return "Analyze pods and deployments"


def test_kubernetes_agent():

    agent = KubernetesAgent(
        MockLLM()
    )

    response = agent.run(
        "Why is my payment service failing?"
    )

    assert response == "Analyze pods and deployments"