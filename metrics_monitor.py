import random
from direct.task import Task

class MetricsMonitor:

    def __init__(self, nodes):

        self.nodes = nodes

    def monitor(self, task):

        for node in self.nodes:

            cpu = random.randint(10, 95)

            if cpu > 75:

                node.setColor(
                    1, 0, 0, 1
                )

            elif cpu > 40:

                node.setColor(
                    1, 1, 0, 1
                )

            else:

                node.setColor(
                    0, 1, 0, 1
                )

        return Task.cont
