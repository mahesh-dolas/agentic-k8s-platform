from tools.kubernetes.client import KubernetesClient


def test_kubernetes_client():

    client = KubernetesClient()

    assert client.get_core_api() is not None

    assert client.get_apps_api() is not None