from agent.core.diagnosis import DiagnosisEngine


def test_diagnosis_engine():

    engine = DiagnosisEngine()


    results = [
        {
            "tool": "kubernetes_pods",
            "result": {
                "pods": [
                    {
                        "name": "payment-service",
                        "state": "CrashLoopBackOff"
                    }
                ]
            }
        }
    ]


    diagnosis = engine.analyze(
        results
    )


    assert "CrashLoopBackOff" in diagnosis["findings"][0]

    assert len(
        diagnosis["recommendations"]
    ) > 0