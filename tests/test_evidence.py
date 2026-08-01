from agent.core.evidence import EvidenceCorrelationEngine



def test_evidence_correlation():


    engine = EvidenceCorrelationEngine()


    investigation = {

        "unhealthy_pods": [

            {
                "name": "payment-service",
                "state": "CrashLoopBackOff"
            }

        ],

        "events": {

            "events": [
                "BackOff restarting container"
            ]

        },

        "logs": [

            {

                "logs": [
                    "Database connection refused"
                ]

            }

        ]

    }


    result = engine.correlate(
        investigation
    )


    assert result["resource"] == "payment-service"

    assert result["severity"] == "high"

    assert len(
        result["evidence"]["logs"]
    ) == 1