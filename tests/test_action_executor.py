from agent.core.action_executor import (
    KubernetesActionExecutor
)



def test_action_blocked_without_approval():


    executor = KubernetesActionExecutor()


    result = executor.execute(
        {
            "approved": False,
            "action": "restart_pod",
            "reason": "Waiting for human approval"
        }
    )


    assert result["status"] == "blocked"