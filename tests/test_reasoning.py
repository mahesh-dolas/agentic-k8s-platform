from agent.core.reasoning import ReasoningEngine



def test_reasoning_engine():

    engine = ReasoningEngine()


    diagnosis = {

        "summary": "Kubernetes diagnostic analysis completed",

        "findings": [
            "payment-service is CrashLoopBackOff"
        ],

        "recommendations": [
            "Check pod logs"
        ]
    }


    result = engine.analyze(
        diagnosis
    )


    assert "summary" in result

    assert len(result["findings"]) == 1

    assert len(result["next_steps"]) > 0