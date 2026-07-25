from agent.core.incident_memory import IncidentMemory



def test_incident_memory():


    memory = IncidentMemory()


    memory.remember(
        {
            "issue": "payment-service CrashLoopBackOff",
            "resolution": "Increase memory limit"
        }
    )


    result = memory.search(
        "payment-service"
    )


    assert len(result) == 1

    assert result[0]["resolution"] == "Increase memory limit"