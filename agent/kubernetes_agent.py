class KubernetesAgent:

    def __init__(self, llm, tool_registry):

        self.llm = llm
        self.tool_registry = tool_registry


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

        available_tools = self.tool_registry.list_tools()

        analysis_prompt = f"""
You are a Kubernetes SRE Agent.

Available tools:

{available_tools}

Analyze the following request:

{request}

Select the appropriate tool.

Return ONLY the tool name.
"""

        tool_name = self.llm.generate(
            analysis_prompt
        )

        result = self.execute_tool(
            tool_name,
            {}
        )

        return result