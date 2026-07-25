class KubernetesAgent:

    def __init__(self, llm, tools=None):
        self.llm = llm
        self.tools = tools or []


    def run(self, request):
        """
        Analyze Kubernetes troubleshooting request
        and generate an execution plan.
        """

        analysis_prompt = f"""
You are a Kubernetes SRE Agent.

Analyze the following Kubernetes issue:

{request}

Determine:

1. What Kubernetes information is required?
2. Which tools should be executed?
3. What troubleshooting steps should be followed?
4. Provide a recommended diagnosis approach.
"""

        plan = self.llm.generate(
            analysis_prompt
        )

        return plan