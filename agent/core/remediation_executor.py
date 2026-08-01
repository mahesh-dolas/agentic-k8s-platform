from tools.kubernetes.remediation.restart_deployment import (
    RestartDeploymentAction
)


class RemediationExecutor:


    def __init__(self):

        self.restart_action = RestartDeploymentAction()



    def execute(self, decision, approval):


        if not approval.get("approved"):

            return {

                "status": "blocked",

                "message": approval.get("reason")

            }


        action = decision.get(
            "action"
        )


        if action == "restart_pod":


            return self.restart_action.execute(
                deployment="nginx-demo",
                namespace="default"
            )


        return {

            "status": "unsupported",

            "action": action

        }