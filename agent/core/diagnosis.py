class DiagnosisEngine:

    ISSUE_MAP = {
        "CrashLoopBackOff": {
            "severity": "Critical",
            "message": "Application is repeatedly crashing.",
            "recommendations": [
                "Check pod logs",
                "Verify environment variables",
                "Check container configuration"
            ]
        },
        "ImagePullBackOff": {
            "severity": "Critical",
            "message": "Unable to pull container image.",
            "recommendations": [
                "Verify image name",
                "Check image registry access",
                "Validate imagePullSecrets"
            ]
        },
        "ErrImagePull": {
            "severity": "Critical",
            "message": "Container image pull failed.",
            "recommendations": [
                "Verify container image exists",
                "Check registry credentials"
            ]
        },
        "Pending": {
            "severity": "Warning",
            "message": "Pod cannot be scheduled.",
            "recommendations": [
                "Check node capacity",
                "Review resource requests",
                "Check node taints"
            ]
        },
        "OOMKilled": {
            "severity": "Critical",
            "message": "Container exceeded memory limit.",
            "recommendations": [
                "Increase memory limits",
                "Review application memory usage"
            ]
        },
        "Failed": {
            "severity": "Critical",
            "message": "Pod failed.",
            "recommendations": [
                "Check pod events",
                "Review application logs"
            ]
        }
    }


    def analyze(self, results):

        findings = []
        recommendations = []


        for item in results:

            tool = item["tool"]
            result = item["result"]


            if tool == "kubernetes_pods":

                for pod in result.get("pods", []):

                    name = pod.get("name")
                    state = pod.get("state")


                    if state != "Running":

                        issue = self.ISSUE_MAP.get(
                            state,
                            {
                                "severity": "Warning",
                                "message": "Unknown pod state.",
                                "recommendations": [
                                    "Inspect pod status"
                                ]
                            }
                        )


                        # Keep string format for backward compatibility
                        findings.append(
                            f"{name} is {state} - "
                            f"{issue['severity']}: "
                            f"{issue['message']}"
                        )


                        recommendations.extend(
                            issue["recommendations"]
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
            "recommendations": list(set(recommendations))
        }