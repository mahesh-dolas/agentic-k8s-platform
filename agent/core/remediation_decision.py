class RemediationDecisionEngine:


    def decide(self, diagnosis):


        decision = {

            "action": "none",

            "confidence": "low",

            "approval_required": True,

            "reason": ""

        }



        incident = diagnosis.get(
            "incident",
            {}
        )


        severity = incident.get(
            "severity"
        )


        symptoms = incident.get(
            "symptoms",
            []
        )



        if (
            severity == "high"
            and
            "CrashLoopBackOff" in symptoms
        ):

            decision["action"] = (
                "restart_pod"
            )


            decision["confidence"] = (
                "high"
            )


            decision["approval_required"] = (
                True
            )


            decision["reason"] = (
                "Pod is continuously restarting"
            )



        elif severity == "medium":


            decision["action"] = (
                "collect_more_logs"
            )


            decision["confidence"] = (
                "medium"
            )


            decision["reason"] = (
                "Need additional evidence"
            )



        return decision