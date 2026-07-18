from tools.registry import ToolRegistry
from tools.kubernetes_tool import KubernetesHealthTool


def test_tool_registry():

    registry = ToolRegistry()

    registry.register(
        KubernetesHealthTool()
    )

    assert (
        "kubernetes_health_check"
        in registry.list_tools()
    )


def test_kubernetes_tool():

    tool = KubernetesHealthTool()

    result = tool.execute(
        "production-cluster"
    )

    assert result["status"] == "healthy"