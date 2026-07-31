from tools.base import Tool
from tools.kubernetes.client import KubernetesClient


class KubernetesLogsTool(Tool):

    @property
    def name(self):
        return "kubernetes_logs"


    @property
    def description(self):
        return "Retrieve Kubernetes pod container logs"


    def __init__(self):

        self.client = KubernetesClient()


    def execute(self, input_data=None):

        if not input_data:
            return {
                "status": "error",
                "message": "Pod information required",
                "logs": []
            }


        pod_name = input_data.get("pod")
        namespace = input_data.get(
            "namespace",
            "default"
        )


        if not pod_name:

            return {
                "status": "error",
                "message": "pod name missing",
                "logs": []
            }


        try:

            core_api = self.client.get_core_api()


            logs = core_api.read_namespaced_pod_log(
                name=pod_name,
                namespace=namespace,
                tail_lines=100
            )


            return {
                "status": "success",
                "pod": pod_name,
                "namespace": namespace,
                "logs": logs.splitlines()
            }


        except Exception as e:

            return {
                "status": "error",
                "message": str(e),
                "logs": []
            }