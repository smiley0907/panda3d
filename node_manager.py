from panda3d.core import TextNode

class NodeManager:

    def __init__(self, base):
        self.base = base
        self.nodes = []

    def create_node(self, node_data):

        node = self.base.loader.loadModel(
            "models/box"
        )

        node.reparentTo(
            self.base.render
        )

        node.setScale(2)

        node.setPos(
            node_data["x"],
            node_data["y"],
            node_data["z"]
        )

        text = TextNode('node_label')
        text.setText(node_data["name"])

        label = self.base.render.attachNewNode(text)

        label.setScale(1)
        label.setPos(
            node_data["x"],
            node_data["y"],
            node_data["z"] + 3
        )

        self.nodes.append(node)

        return node
