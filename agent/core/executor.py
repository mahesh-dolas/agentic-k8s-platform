# class Executor:

#     def execute(self, plan):

#         return {
#             "status": "completed",
#             "steps_executed": plan["steps"]
#         }

from tools.registry import ToolRegistry


class Executor:

    def __init__(self, tool_registry=None):

        self.tool_registry = tool_registry


    def execute(self, plan):

        results = []

        for step in plan["steps"]:

            if (
                self.tool_registry
                and self.tool_registry.get_tool(step)
            ):

                tool = self.tool_registry.get_tool(step)

                result = tool.execute(
                    "default"
                )

                results.append(result)

            else:

                results.append(
                    {
                        "step": step,
                        "status": "completed"
                    }
                )

        return {
            "status": "completed",
            "results": results
        }