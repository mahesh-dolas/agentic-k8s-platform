from agent.core.kubernetes_planner import KubernetesPlanner
from agent.core.diagnosis import DiagnosisEngine


class KubernetesAgent:

    def __init__(self, llm, tool_registry):

        self.llm = llm
        self.tool_registry = tool_registry
        self.planner = KubernetesPlanner()
        self.diagnosis = DiagnosisEngine()


    def execute_tool(self, tool_name, input_data=None):

        tool = self.tool_registry.get_tool(
            tool_name
        )

        if not tool:
            return {
                "error": f"Tool '{tool_name}' not found"
            }

        return tool.execute(
            input_data
        )


    def run(self, request):

        plan = self.planner.create_plan(
            request
        )

        results = []

        for step in plan:

            result = self.execute_tool(
                step["tool"],
                {}
            )

            results.append(
                {
                    "tool": step["tool"],
                    "reason": step["reason"],
                    "result": result
                }
            )

        return self.diagnosis.analyze(
            results
        )