from tools.kubernetes.pods_tool import KubernetesPodsTool


def test_live_kubernetes_pods():

    tool = KubernetesPodsTool()

    result = tool.execute({})


    assert result["status"] == "success"

    assert "pods" in result

    assert len(result["pods"]) > 0