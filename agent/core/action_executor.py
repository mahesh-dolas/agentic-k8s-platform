class KubernetesActionExecutor:


    def execute(self, approval):


        if not approval.get(
            "approved"
        ):

            return {

                "status": "blocked",

                "message": approval.get(
                    "reason"
                )

            }


        action = approval.get(
            "action"
        )


        if action == "restart_pod":

            return {

                "status": "executed",

                "action": "restart_pod",

                "message": (
                    "Pod restart action executed"
                )

            }


        return {

            "status": "unknown",

            "message": (
                f"Unsupported action {action}"
            )

        }