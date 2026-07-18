# class Agent:

#     def __init__(self, name):
#         self.name = name
#         self.memory = []
#         self.tools = []

#     def think(self, task):
#         """
#         Create execution plan
#         """
#         return {
#             "agent": self.name,
#             "task": task,
#             "status": "planning"
#         }


#     def execute(self, task):
#         """
#         Execute agent workflow
#         """
#         plan = self.think(task)

#         return {
#             "plan": plan,
#             "result": "Task executed"
#         }


# if __name__ == "__main__":

#     agent = Agent("Kubernetes-AI-Agent")

#     response = agent.execute(
#         "Analyze Kubernetes cluster health"
#     )

#     print(response)

# from agent.core.planner import Planner
# from agent.core.executor import Executor


# class Agent:

#     def __init__(self, name):

#         self.name = name
#         self.planner = Planner()
#         self.executor = Executor()


#     def run(self, task):

#         plan = self.planner.create_plan(task)

#         result = self.executor.execute(plan)

#         return {
#             "agent": self.name,
#             "plan": plan,
#             "result": result
#         }

from agent.core.planner import Planner
from agent.core.executor import Executor


class Agent:

    def __init__(self, name, tool_registry=None):

        self.name = name
        self.planner = Planner()

        self.executor = Executor(
            tool_registry
        )


    def run(self, task):

        plan = self.planner.create_plan(task)

        result = self.executor.execute(
            plan
        )

        return {
            "agent": self.name,
            "plan": plan,
            "result": result
        }