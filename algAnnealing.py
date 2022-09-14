import random as rm


class algAnnealing:

    def __init__(self, initialData):

        # в data храним исходные данные
        self.data = initialData
        # в memberType содержится решение и энергия
        self.memberType = {
            "solution": [i for i in range(int(self.data["sizeBoard"]))],
            "energy": 0.0
        }

        for i in range(int(self.data["sizeBoard"])):
            self.tweakSolution()

    def tweakSolution(self):
        x = rm.randint(self.data["sizeBoard"])
        y = rm.randint(self.data["sizeBoard"])
        while y != x:
            self.memberType["solution"][x], self.memberType["solution"][y] = self.memberType["solution"][y], self.memberType["solution"][x]
            y = rm.randint(self.data["sizeBoard"])

    def computeEnergy(self):

        dx = [-1, 1, -1, 1]
        dy = [-1, 1, -1, 1]
