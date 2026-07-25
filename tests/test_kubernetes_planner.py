from agent.core.kubernetes_planner import KubernetesPlanner


def test_kubernetes_planner():

    planner = KubernetesPlanner()

    plan = planner.create_plan(
        "Application failure in Kubernetes"
    )

    assert len(plan) == 2

    assert plan[0]["tool"] == "kubernetes_health"

    assert plan[1]["tool"] == "kubernetes_events"