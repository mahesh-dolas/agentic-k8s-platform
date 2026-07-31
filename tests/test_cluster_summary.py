from agent.core.cluster_summary import ClusterHealthSummary



def test_cluster_health_summary():

    summary_engine = ClusterHealthSummary()


    diagnosis = {
        "findings": [
            "payment-service is CrashLoopBackOff - Critical"
        ],
        "recommendations": [
            "Check pod logs"
        ]
    }


    result = summary_engine.generate(
        diagnosis
    )


    assert result["cluster_status"] == "CRITICAL"

    assert result["total_issues"] == 1

    assert "CrashLoopBackOff" in result["issues"][0]