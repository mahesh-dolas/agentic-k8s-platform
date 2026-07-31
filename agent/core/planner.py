# class Planner:

#     def create_plan(self, task):

#         return {
#             "task": task,
#             "steps": [
#                 "Understand request",
#                 "Create execution strategy",
#                 "Execute actions",
#                 "Return response"
#             ]
#         }

class Planner:

    def create_plan(self, task):

        if "kubernetes" in task.lower():

            return {
                "task": task,
                "steps": [
                    "kubernetes_health_check"
                ]
            }


        return {
            "task": task,
            "steps": [
                "analyze_request"
            ]
        }