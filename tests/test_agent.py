from agent.core.agent import Agent
from tools.registry import ToolRegistry
from tools.kubernetes_tool import KubernetesHealthTool


def test_agent_tool_execution():

    registry = ToolRegistry()

    registry.register(
        KubernetesHealthTool()
    )


    agent = Agent(
        "Kubernetes-AI-Agent",
        registry
    )


    response = agent.run(
        "Check Kubernetes cluster health"
    )


    assert (
        response["result"]["status"]
        == "completed"
    )