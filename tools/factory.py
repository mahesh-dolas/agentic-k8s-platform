from tools.registry import ToolRegistry
from tools.kubernetes.health_tool import KubernetesHealthTool


def create_tool_registry():

    registry = ToolRegistry()

    registry.register(
        KubernetesHealthTool()
    )

    return registry