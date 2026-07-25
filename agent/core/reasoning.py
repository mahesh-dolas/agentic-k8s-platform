class ReasoningEngine:


    def analyze(self, diagnosis):

        findings = diagnosis.get(
            "findings",
            []
        )


        recommendations = diagnosis.get(
            "recommendations",
            []
        )


        previous = diagnosis.get(
            "previous_incidents",
            []
        )


        if previous:

            summary = (
                "Similar previous incidents found. "
                "Using historical troubleshooting context."
            )

        elif findings:

            summary = (
                "Kubernetes issue detected. "
                "The agent analyzed cluster signals."
            )

        else:

            summary = (
                "Kubernetes cluster appears healthy."
            )


        return {

            "summary": summary,

            "findings": findings,

            "recommendations": recommendations,

            "previous_incidents": previous,

            "next_steps": [
                "Review application logs",
                "Check deployment configuration",
                "Monitor pod health"
            ]
        }