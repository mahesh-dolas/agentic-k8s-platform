from tools.base import Tool
from tools.kubernetes.client import KubernetesClient


class KubernetesEventsTool(Tool):

    @property
    def name(self):
        return "kubernetes_events"


    @property
    def description(self):
        return "Analyze Kubernetes cluster events"


    def __init__(self):

        self.client = KubernetesClient()


    def execute(self, input_data=None):

        events = []

        try:

            core_api = self.client.get_core_api()

            event_list = core_api.list_event_for_all_namespaces()


            for event in event_list.items:

                events.append(
                    {
                        "namespace": event.metadata.namespace,
                        "name": event.metadata.name,
                        "type": event.type,
                        "reason": event.reason,
                        "message": event.message
                    }
                )


            return {
                "status": "success",
                "events": events
            }


        except Exception as e:

            return {
                "status": "error",
                "message": str(e),
                "events": []
            }