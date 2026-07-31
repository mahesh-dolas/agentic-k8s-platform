class RemediationEngine:


    REMEDIATION_MAP = {

        "restart": {
            "action": "restart_pod",
            "priority": "High",
            "category": "Recovery",
            "description": "Restart unhealthy pod after validation"
        },

        "logs": {
            "action": "check_pod_logs",
            "priority": "High",
            "category": "Troubleshooting",
            "description": "Inspect pod logs for application errors"
        },

        "environment": {
            "action": "validate_configuration",
            "priority": "Medium",
            "category": "Configuration",
            "description": "Check environment variables and configuration"
        },

        "image": {
            "action": "verify_container_image",
            "priority": "High",
            "category": "Container",
            "description": "Validate image name and registry access"
        },

        "memory": {
            "action": "adjust_memory_limits",
            "priority": "Medium",
            "category": "Resource Management",
            "description": "Review and adjust memory limits"
        },

        "scale": {
            "action": "scale_deployment",
            "priority": "Medium",
            "category": "Scaling",
            "description": "Increase or decrease deployment replicas"
        }
    }


    def evaluate(self, diagnosis):

        recommendations = diagnosis.get(
            "recommendations",
            []
        )

        actions = []
        processed = set()


        for recommendation in recommendations:

            recommendation_lower = recommendation.lower()


            for keyword, remediation in self.REMEDIATION_MAP.items():

                if keyword in recommendation_lower:

                    action_name = remediation["action"]

                    if action_name in processed:
                        continue

                    actions.append(
                        {
                            "action": action_name,
                            "priority": remediation["priority"],
                            "category": remediation["category"],
                            "description": remediation["description"],
                            "approval_required": True
                        }
                    )

                    processed.add(action_name)


        return {
            "recommended_actions": actions
        }