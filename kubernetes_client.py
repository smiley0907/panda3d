from kubernetes import client
from kubernetes import config

class KubernetesClient:

    def get_nodes(self):

        config.load_kube_config()

        v1 = client.CoreV1Api()

        nodes = []

        for node in v1.list_node().items:

            nodes.append(
                node.metadata.name
            )

        return nodes
