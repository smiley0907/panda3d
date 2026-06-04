class PodManager:

    def __init__(self, base):
        self.base = base

    def create_pod(self, x, y, z):

        pod = self.base.loader.loadModel(
            "models/smiley"
        )

        pod.reparentTo(
            self.base.render
        )

        pod.setScale(0.6)

        pod.setPos(
            x,
            y,
            z
        )

        return pod
