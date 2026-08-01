from agent.core.investigation import InvestigationEngine



class MockTool:


    def __init__(self, response):

        self.response = response



    def execute(self, data):

        return self.response



class MockRegistry:


    def get_tool(self, name):

        if name == "kubernetes_pods":

            return MockTool(
                {
                    "pods": [
                        {
                            "name": "payment-service",
                            "state": "CrashLoopBackOff"
                        }
                    ]
                }
            )


        if name == "kubernetes_events":

            return MockTool(
                {
                    "events": [
                        "BackOff restarting container"
                    ]
                }
            )



def test_investigation_engine():


    engine = InvestigationEngine(
        MockRegistry()
    )


    result = engine.investigate()


    assert len(
        result["unhealthy_pods"]
    ) == 1


    assert (
        result["unhealthy_pods"][0]["state"]
        == "CrashLoopBackOff"
    )