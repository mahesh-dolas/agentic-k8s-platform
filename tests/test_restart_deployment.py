from tools.kubernetes.remediation.restart_deployment import (
    RestartDeploymentAction
)



def test_restart_requires_deployment():


    action = RestartDeploymentAction()


    result = action.execute(
        None
    )


    assert result["status"] == "error"

    assert (
        result["message"]
        ==
        "Deployment name required"
    )