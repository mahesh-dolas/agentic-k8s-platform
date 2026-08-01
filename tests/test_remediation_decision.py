from agent.core.kubernetes_planner import KubernetesPlanner
from agent.core.diagnosis import DiagnosisEngine
from agent.core.reasoning import ReasoningEngine
from agent.core.incident_memory import IncidentMemory
from agent.core.remediation import RemediationEngine
from agent.core.cluster_summary import ClusterHealthSummary
from agent.core.investigation import InvestigationEngine
from agent.core.evidence import EvidenceCorrelationEngine
from agent.core.remediation_decision import RemediationDecisionEngine


class KubernetesAgent:

    def __init__(self, llm, tool_registry):

        self.llm = llm
        self.tool_registry = tool_registry

        self.planner = KubernetesPlanner()

        self.diagnosis = DiagnosisEngine()

        self.reasoning = ReasoningEngine()

        self.memory = IncidentMemory()

        self.remediation = RemediationEngine()

        # Phase 7.5.6
        self.remediation_decision = RemediationDecisionEngine()

        self.summary = ClusterHealthSummary()


        # Phase 7.5 Autonomous Investigation
        self.investigation = InvestigationEngine(
            tool_registry
        )


        # Phase 7.5.4 Evidence Correlation
        self.evidence = EvidenceCorrelationEngine()



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



        # 2. Correlate evidence

        incident_evidence = self.evidence.correlate(
            investigation
        )



        # 3. Create execution plan

        plan = self.planner.create_plan(
            request
        )


        results = []



        # 4. Execute Kubernetes tools

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



        # 5. Diagnose Kubernetes state

        diagnosis = self.diagnosis.analyze(
            results
        )


        diagnosis["investigation"] = investigation

        diagnosis["incident"] = incident_evidence



        # 6. Check previous incidents

        similar_incidents = self.memory.search(
            request
        )


        diagnosis["previous_incidents"] = similar_incidents



        # 7. Generate reasoning

        final_response = self.reasoning.analyze(
            diagnosis
        )



        # 8. Generate remediation recommendations

        remediation_plan = self.remediation.evaluate(
            diagnosis
        )



        # 9. Generate autonomous remediation decision

        remediation_decision = self.remediation_decision.decide(
            diagnosis
        )



        # 10. Cluster health summary

        cluster_summary = self.summary.generate(
            diagnosis,
            remediation_plan
        )



        # 11. Final response

        final_response["cluster_health"] = (
            cluster_summary
        )


        final_response["investigation"] = (
            investigation
        )


        final_response["incident"] = (
            incident_evidence
        )


        final_response["remediation"] = (
            remediation_plan
        )


        final_response["remediation_decision"] = (
            remediation_decision
        )



        # 12. Store incident memory

        self.memory.remember(
            {
                "issue": request,
                "resolution": final_response["recommendations"]
            }
        )



        return final_response