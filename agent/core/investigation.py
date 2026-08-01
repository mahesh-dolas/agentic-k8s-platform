from tools.kubernetes.logs_tool import KubernetesLogsTool


class InvestigationEngine:


    def __init__(self, tool_registry):

        self.tool_registry = tool_registry

        self.logs_tool = KubernetesLogsTool()



    def investigate(self):

        findings = {}


        # 1. Collect pod information

        pods_tool = self.tool_registry.get_tool(
            "kubernetes_pods"
        )

        pods_result = pods_tool.execute({})


        findings["pods"] = pods_result



        # 2. Collect Kubernetes events

        events_tool = self.tool_registry.get_tool(
            "kubernetes_events"
        )

        events_result = events_tool.execute({})


        findings["events"] = events_result



        # 3. Identify unhealthy pods

        unhealthy_pods = []


        for pod in pods_result.get(
            "pods",
            []
        ):

            pod_state = pod.get(
                "state",
                pod.get(
                    "status"
                )
            )


            if pod_state not in [
                "Running",
                "Succeeded"
            ]:

                unhealthy_pods.append(
                    pod
                )


        findings["unhealthy_pods"] = unhealthy_pods



        # 4. Automatically collect logs

        pod_logs = []


        for pod in unhealthy_pods:

            pod_name = pod.get(
                "name"
            )


            namespace = pod.get(
                "namespace",
                "default"
            )


            if pod_name:

                logs = self.logs_tool.execute(
                    {
                        "pod": pod_name,
                        "namespace": namespace
                    }
                )


                pod_logs.append(
                    logs
                )


        findings["logs"] = pod_logs



        return findings