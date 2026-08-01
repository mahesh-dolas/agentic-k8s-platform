from tools.kubernetes.events_tool import KubernetesEventsTool


def test_live_kubernetes_events():

    tool = KubernetesEventsTool()

    result = tool.execute({})


    assert result["status"] == "success"

    assert "events" in result