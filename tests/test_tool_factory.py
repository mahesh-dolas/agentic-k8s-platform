from tools.factory import create_tool_registry


def test_tool_factory():

    registry = create_tool_registry()

    tool = registry.get_tool(
        "kubernetes_health"
    )

    assert tool is not None

    result = tool.execute({})

    assert result["status"] == "healthy"