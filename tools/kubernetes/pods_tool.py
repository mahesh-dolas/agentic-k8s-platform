from tools.base import Tool


class KubernetesPodsTool(Tool):

    @property
    def name(self):
        return "kubernetes_pods"


    @property
    def description(self):
        return "Analyze Kubernetes pod status"


    def execute(self, input_data):

        return {
            "status": "warning",
            "pods": [
                {
                    "name": "payment-service",
                    "state": "CrashLoopBackOff"
                },
                {
                    "name": "user-service",
                    "state": "Running"
                }
            ]
        }