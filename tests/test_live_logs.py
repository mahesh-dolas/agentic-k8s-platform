from tools.kubernetes.logs_tool import KubernetesLogsTool


def test_live_kubernetes_logs():

    tool = KubernetesLogsTool()

    result = tool.execute(
        {
            "pod": "metrics-server-v1.35.1-7d5b67dddc-w5m7t",
            "namespace": "kube-system"
        }
    )

    assert result["status"] == "success"

    assert "logs" in result

    assert len(result["logs"]) > 0