from tools.kubernetes.remediation.restart_deployment import (
    RestartDeploymentAction
)


def test_restart_nginx_deployment():

    action = RestartDeploymentAction()


    result = action.execute(
        "nginx-demo",
        "default"
    )


    assert result["status"] == "success"

    assert result["deployment"] == "nginx-demo"