import json

class ConfigLoader:

    @staticmethod
    def load_cluster_config():

        with open("config/cluster.json") as f:
            return json.load(f)
