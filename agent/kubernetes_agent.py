from agent.core.kubernetes_planner import KubernetesPlanner
from agent.core.diagnosis import DiagnosisEngine
from agent.core.reasoning import ReasoningEngine
from agent.core.incident_memory import IncidentMemory
from agent.core.remediation import RemediationEngine


class KubernetesAgent:

    def __init__(self, llm, tool_registry):

        self.llm = llm
        self.tool_registry = tool_registry

        self.planner = KubernetesPlanner()

        self.diagnosis = DiagnosisEngine()

        self.reasoning = ReasoningEngine()

        self.memory = IncidentMemory()

        self.remediation = RemediationEngine()


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

        # 1. Create execution plan

        plan = self.planner.create_plan(
            request
        )


        results = []


        # 2. Execute Kubernetes tools

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


        # 3. Diagnose results

        diagnosis = self.diagnosis.analyze(
            results
        )


        # 4. Check previous incidents

        similar_incidents = self.memory.search(
            request
        )


        diagnosis["previous_incidents"] = similar_incidents


        # 5. Generate reasoning response

        final_response = self.reasoning.analyze(
            diagnosis
        )


        # 6. Generate remediation plan

        remediation_plan = self.remediation.evaluate(
            diagnosis
        )


        final_response["remediation"] = remediation_plan


        # 7. Store incident memory

        self.memory.remember(
            {
                "issue": request,
                "resolution": final_response["recommendations"]
            }
        )


        return final_response