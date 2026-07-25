from agent.core.kubernetes_planner import KubernetesPlanner
from agent.core.diagnosis import DiagnosisEngine
from agent.core.reasoning import ReasoningEngine
from agent.core.incident_memory import IncidentMemory


class KubernetesAgent:

    def __init__(self, llm, tool_registry):

        self.llm = llm
        self.tool_registry = tool_registry

        self.planner = KubernetesPlanner()

        self.diagnosis = DiagnosisEngine()

        self.reasoning = ReasoningEngine()

        self.memory = IncidentMemory()


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

        # Step 1: Create execution plan

        plan = self.planner.create_plan(
            request
        )


        results = []


        # Step 2: Execute Kubernetes tools

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


        # Step 3: Analyze tool results

        diagnosis = self.diagnosis.analyze(
            results
        )


        # Step 4: Search previous incidents

        similar_incidents = self.memory.search(
            request
        )


        diagnosis["previous_incidents"] = similar_incidents


        # Step 5: Generate AI SRE response

        final_response = self.reasoning.analyze(
            diagnosis
        )


        # Step 6: Store current incident

        self.memory.remember(
            {
                "issue": request,
                "resolution": final_response["recommendations"]
            }
        )


        return final_response