from config_loader import ConfigLoader
from node_manager import NodeManager
from pod_manager import PodManager

class Cluster:

    def __init__(self, base):

        self.base = base

        self.node_manager = NodeManager(base)
        self.pod_manager = PodManager(base)

    def load_cluster(self):

        data = ConfigLoader.load_cluster_config()

        for node in data["nodes"]:

            self.node_manager.create_node(node)

        self.create_sample_pods()

    def create_sample_pods(self):

        self.pod_manager.create_pod(
            15, 5, 0
        )

        self.pod_manager.create_pod(
            15, -5, 0
        )

        self.pod_manager.create_pod(
            -15, 5, 0
        )

        self.pod_manager.create_pod(
            -15, -5, 0
        )
