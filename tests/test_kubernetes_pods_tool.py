from tools.factory import create_tool_registry


def test_kubernetes_pods_tool():

    registry = create_tool_registry()

    tool = registry.get_tool(
        "kubernetes_pods"
    )

    result = tool.execute({})

    assert result["status"] == "warning"
    assert len(result["pods"]) == 2