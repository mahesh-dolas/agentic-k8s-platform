from tools.kubernetes.logs_tool import KubernetesLogsTool
from tools.registry import ToolRegistry
from tools.kubernetes.health_tool import KubernetesHealthTool
from tools.kubernetes.events_tool import KubernetesEventsTool
from tools.kubernetes.pods_tool import KubernetesPodsTool
from tools.kubernetes.remediation.actions import (
    KubernetesRestartPodTool,
    KubernetesScaleDeploymentTool
)


def create_tool_registry():

    registry = ToolRegistry()

    registry.register(
        KubernetesHealthTool()
    )
    registry.register(
        KubernetesEventsTool()
    )
    registry.register(
        KubernetesPodsTool()
    )
    registry.register(
    KubernetesRestartPodTool()
    )
    registry.register(
    KubernetesScaleDeploymentTool()
    )
    registry.register(
    KubernetesLogsTool()
    )   

    return registry