from tools.kubernetes.client import KubernetesClient
from datetime import datetime


class RestartDeploymentAction:


    def __init__(self):

        self.client = KubernetesClient()



    def execute(
        self,
        deployment,
        namespace="default"
    ):


        if not deployment:

            return {

                "status": "error",

                "message": "Deployment name required"

            }


        try:

            apps_api = self.client.get_apps_api()


            body = {

                "spec": {

                    "template": {

                        "metadata": {

                            "annotations": {

                                "kubectl.kubernetes.io/restartedAt":
                                datetime.utcnow().isoformat()

                            }

                        }

                    }

                }

            }


            apps_api.patch_namespaced_deployment(
                name=deployment,
                namespace=namespace,
                body=body
            )


            return {

                "status": "success",

                "action": "restart_deployment",

                "deployment": deployment,

                "namespace": namespace

            }



        except Exception as e:


            return {

                "status": "error",

                "message": str(e)

            }