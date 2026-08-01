from agent.core.kubernetes_planner import KubernetesPlanner
from agent.core.diagnosis import DiagnosisEngine
from agent.core.reasoning import ReasoningEngine
from agent.core.incident_memory import IncidentMemory
from agent.core.remediation import RemediationEngine
from agent.core.cluster_summary import ClusterHealthSummary
from agent.core.investigation import InvestigationEngine


class KubernetesAgent:

    def __init__(self, llm, tool_registry):

        self.llm = llm
        self.tool_registry = tool_registry

        self.planner = KubernetesPlanner()

        self.diagnosis = DiagnosisEngine()

        self.reasoning = ReasoningEngine()

        self.memory = IncidentMemory()

        self.remediation = RemediationEngine()

        self.summary = ClusterHealthSummary()

        # Phase 7.5 - Autonomous Investigation Engine
        self.investigation = InvestigationEngine(
            tool_registry
        )


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

        # 1. Autonomous Kubernetes investigation
        investigation = self.investigation.investigate()


        # 2. Create execution plan

        plan = self.planner.create_plan(
            request
        )


        results = []


        # 3. Execute Kubernetes tools

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


        # 4. Diagnose Kubernetes results

        diagnosis = self.diagnosis.analyze(
            results
        )


        # Add investigation evidence

        diagnosis["investigation"] = investigation


        # 5. Check previous incidents

        similar_incidents = self.memory.search(
            request
        )


        diagnosis["previous_incidents"] = similar_incidents


        # 6. Generate reasoning response

        final_response = self.reasoning.analyze(
            diagnosis
        )


        # 7. Generate remediation plan

        remediation_plan = self.remediation.evaluate(
            diagnosis
        )


        # 8. Generate unified cluster health summary

        cluster_summary = self.summary.generate(
            diagnosis,
            remediation_plan
        )


        # 9. Combine final response

        final_response["cluster_health"] = cluster_summary

        final_response["investigation"] = investigation

        final_response["remediation"] = remediation_plan


        # 10. Store incident memory

        self.memory.remember(
            {
                "issue": request,
                "resolution": final_response["recommendations"]
            }
        )


        return final_response