from agent.core.agent import Agent


def test_agent_execution():

    agent = Agent("Kubernetes-AI-Agent")

    response = agent.run(
        "Check Kubernetes cluster health"
    )

    assert response["agent"] == "Kubernetes-AI-Agent"
    assert response["result"]["status"] == "completed"