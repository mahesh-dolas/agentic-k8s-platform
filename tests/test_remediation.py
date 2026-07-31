from tools.factory import create_tool_registry


def test_restart_pod_tool():

    registry = create_tool_registry()

    tool = registry.get_tool(
        "restart_pod"
    )

    result = tool.execute(
        {
            "pod": "payment-service"
        }
    )


    assert result["status"] == "simulated"

    assert result["action"] == "restart_pod"