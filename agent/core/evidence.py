class EvidenceCorrelationEngine:


    def correlate(self, investigation):


        incident = {

            "resource": None,

            "severity": "unknown",

            "symptoms": [],

            "evidence": {

                "events": [],

                "logs": []

            }

        }


        unhealthy_pods = investigation.get(
            "unhealthy_pods",
            []
        )


        if unhealthy_pods:

            pod = unhealthy_pods[0]


            incident["resource"] = pod.get(
                "name"
            )


            state = pod.get(
                "state",
                pod.get(
                    "status"
                )
            )


            incident["symptoms"].append(
                state
            )


            if state in [
                "CrashLoopBackOff",
                "Error"
            ]:

                incident["severity"] = "high"



        events = investigation.get(
            "events",
            {}
        )


        incident["evidence"]["events"] = events.get(
            "events",
            []
        )



        logs = investigation.get(
            "logs",
            []
        )


        for item in logs:

            incident["evidence"]["logs"].extend(
                item.get(
                    "logs",
                    []
                )
            )


        return incident