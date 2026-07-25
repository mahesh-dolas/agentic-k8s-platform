from tools.factory import create_tool_registry


def test_kubernetes_events_tool():

    registry = create_tool_registry()

    tool = registry.get_tool(
        "kubernetes_events"
    )

    result = tool.execute({})

    assert result["status"] == "warning"