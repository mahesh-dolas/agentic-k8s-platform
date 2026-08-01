from tools.base import Tool
from tools.kubernetes.client import KubernetesClient


class KubernetesPodsTool(Tool):

    @property
    def name(self):
        return "kubernetes_pods"


    @property
    def description(self):
        return "Analyze Kubernetes pod status"


    def __init__(self):

        self.client = KubernetesClient()


    def execute(self, input_data=None):

        pods = []

        try:

            core_api = self.client.get_core_api()

            pod_list = core_api.list_pod_for_all_namespaces()


            for pod in pod_list.items:

                state = "Unknown"


                if pod.status.phase:
                    state = pod.status.phase


                # Detect CrashLoopBackOff, ImagePullBackOff, etc.
                if pod.status.container_statuses:

                    for container in pod.status.container_statuses:

                        if container.state.waiting:

                            state = (
                                container.state.waiting.reason
                            )


                pods.append(
                    {
                        "name": pod.metadata.name,
                        "namespace": pod.metadata.namespace,
                        "state": state
                    }
                )


            return {
                "status": "success",
                "pods": pods
            }


        except Exception as e:

            return {
                "status": "error",
                "message": str(e),
                "pods": []
            }