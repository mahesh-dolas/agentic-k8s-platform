from agent.core.approval import ApprovalGate



def test_approval_required():


    gate = ApprovalGate()


    decision = {

        "action": "restart_pod",

        "approval_required": True

    }


    result = gate.check(
        decision
    )


    assert result["approved"] is False

    assert (
        result["reason"]
        ==
        "Waiting for human approval"
    )