from agent.core.remediation import RemediationEngine


def test_remediation_engine():

    engine = RemediationEngine()


    diagnosis = {
        "recommendations": [
            "Restart unhealthy pod"
        ]
    }


    result = engine.evaluate(
        diagnosis
    )


    assert len(
        result["recommended_actions"]
    ) == 1


    assert (
        result["recommended_actions"][0]["action"]
        == "restart_pod"
    )


    assert (
        result["recommended_actions"][0]["approval_required"]
        is True
    )