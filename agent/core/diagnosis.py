class DiagnosisEngine:

    def analyze(self, results):

        findings = []
        recommendations = []

        for item in results:

            tool = item["tool"]
            result = item["result"]


            if tool == "kubernetes_pods":

                for pod in result.get("pods", []):

                    if pod["state"] != "Running":

                        findings.append(
                            f"{pod['name']} is {pod['state']}"
                        )

                        recommendations.append(
                            "Check pod logs and container configuration"
                        )


            if tool == "kubernetes_events":

                for event in result.get("events", []):

                    findings.append(
                        event
                    )


        if not findings:

            findings.append(
                "No Kubernetes issues detected"
            )


        if not recommendations:

            recommendations.append(
                "Continue monitoring cluster health"
            )


        return {
            "summary": "Kubernetes diagnostic analysis completed",
            "findings": findings,
            "recommendations": recommendations
        }