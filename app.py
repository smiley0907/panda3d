from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode
import json

class K8sVisualizer(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()

        self.camera.setPos(0, -60, 25)
        self.camera.lookAt(0, 0, 0)

        self.load_cluster()

    def load_cluster(self):

        with open("cluster.json") as f:
            data = json.load(f)

        for node in data["nodes"]:
            self.create_node(node)

    def create_node(self, node):

        cube = self.loader.loadModel("models/box")
        cube.reparentTo(self.render)

        cube.setScale(2)
        cube.setPos(
            node["x"],
            node["y"],
            node["z"]
        )

        text = TextNode('node')
        text.setText(node["name"])

        textNodePath = render.attachNewNode(text)
        textNodePath.setScale(1)
        textNodePath.setPos(
            node["x"],
            node["y"],
            node["z"] + 3
        )

app = K8sVisualizer()
app.run()
