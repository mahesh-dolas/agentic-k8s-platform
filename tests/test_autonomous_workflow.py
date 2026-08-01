from agent.core.remediation_decision import (
    RemediationDecisionEngine
)

from agent.core.approval import (
    ApprovalGate
)

from agent.core.action_executor import (
    KubernetesActionExecutor
)



def test_autonomous_workflow():


    decision_engine = RemediationDecisionEngine()

    approval_gate = ApprovalGate()

    executor = KubernetesActionExecutor()



    diagnosis = {

        "incident": {

            "severity": "high",

            "symptoms": [
                "CrashLoopBackOff"
            ]

        }

    }



    decision = decision_engine.decide(
        diagnosis
    )


    approval = approval_gate.check(
        decision
    )


    execution = executor.execute(
        approval
    )



    assert decision["action"] == "restart_pod"

    assert approval["approved"] is False

    assert execution["status"] == "blocked"