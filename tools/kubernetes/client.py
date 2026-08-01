from kubernetes import client, config


class KubernetesClient:

    def __init__(self):

        self.core_api = None
        self.apps_api = None

        self.connect()


    def connect(self):

        try:
            # Local kubeconfig (Mac/Linux/Windows)
            config.load_kube_config()

            print("Connected using kubeconfig")

        except Exception:

            try:
                # Running inside Kubernetes
                config.load_incluster_config()

                print("Connected using in-cluster configuration")

            except Exception as e:

                raise RuntimeError(
                    f"Unable to connect to Kubernetes: {e}"
                )

        self.core_api = client.CoreV1Api()

        self.apps_api = client.AppsV1Api()


    def get_core_api(self):

        return self.core_api


    def get_apps_api(self):

        return self.apps_api