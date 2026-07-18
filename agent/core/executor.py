class Executor:

    def execute(self, plan):

        return {
            "status": "completed",
            "steps_executed": plan["steps"]
        }