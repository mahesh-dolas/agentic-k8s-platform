from agent.core.remediation_executor import (
    RemediationExecutor
)


def test_blocked_without_approval():

    executor = RemediationExecutor()


    result = executor.execute(
        {
            "action": "restart_pod"
        },
        {
            "approved": False,
            "reason": "Waiting approval"
        }
    )


    assert result["status"] == "blocked"