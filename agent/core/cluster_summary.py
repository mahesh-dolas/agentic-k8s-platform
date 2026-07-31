class ClusterHealthSummary:


    def generate(self, diagnosis, remediation=None):

        findings = diagnosis.get(
            "findings",
            []
        )

        recommendations = diagnosis.get(
            "recommendations",
            []
        )


        if not findings:

            status = "HEALTHY"
            summary = "Cluster is healthy"

        else:

            status = self._calculate_status(
                findings
            )

            summary = "Cluster requires attention"


        response = {
            "cluster_status": status,
            "total_issues": len(findings),
            "summary": summary,
            "issues": findings,
            "recommendations": recommendations
        }


        if remediation:

            response["recommended_actions"] = remediation.get(
                "recommended_actions",
                []
            )


        return response



    def _calculate_status(self, findings):

        critical_keywords = [
            "Critical",
            "CrashLoopBackOff",
            "ImagePullBackOff",
            "OOMKilled"
        ]


        for finding in findings:

            for keyword in critical_keywords:

                if keyword.lower() in finding.lower():

                    return "CRITICAL"


        return "WARNING"