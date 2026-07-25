class KubernetesPlanner:

    def __init__(self, llm=None):

        self.llm = llm


    def create_plan(self, request):

        if "health" in request.lower():
            return [
                {
                    "tool": "kubernetes_health",
                    "reason": "Check Kubernetes cluster health"
                }
            ]

        if "failure" in request.lower() or "issue" in request.lower():
            return [
                {
                    "tool": "kubernetes_health",
                    "reason": "Check cluster health"
                },
                {
                    "tool": "kubernetes_events",
                    "reason": "Check Kubernetes events"
                }
            ]

        return [
            {
               "tool": "kubernetes_health",
               "reason": "Check cluster health"
           },
            {
                "tool": "kubernetes_events",
                "reason": "Check Kubernetes events"
            },
           {
                "tool": "kubernetes_pods",
                "reason": "Analyze pod failures"
           }
]