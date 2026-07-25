class RemediationEngine:


    def evaluate(self, diagnosis):

        recommendations = diagnosis.get(
            "recommendations",
            []
        )


        actions = []


        for recommendation in recommendations:

            if "restart" in recommendation.lower():

                actions.append(
                    {
                        "action": "restart_pod",
                        "approval_required": True
                    }
                )


            if "scale" in recommendation.lower():

                actions.append(
                    {
                        "action": "scale_deployment",
                        "approval_required": True
                    }
                )


        return {
            "recommended_actions": actions
        }