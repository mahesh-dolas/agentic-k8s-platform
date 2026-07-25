class KubernetesAgent:

    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools


    def run(self, request):
        """
        Execute Kubernetes troubleshooting request
        """

        analysis_prompt = f"""
You are a Kubernetes SRE Agent.

Analyze the following request:

{request}

Determine:
1. What Kubernetes information is required?
2. Which tools should be executed?
3. What is the troubleshooting approach?
"""

        plan = self.llm.generate(analysis_prompt)

        return plan