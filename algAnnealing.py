import random as rm
import math

from functools import reduce


class algAnnealing:

    def __init__(self, initialData):

        # в data храним исходные данные
        self.data = initialData
        # в memberType содержится решение и энергия
        self.current = {
            "solution": [i for i in range(int(self.data["sizeBoard"]))],
            "energy": 0.0
        }

        self.temp = []
        self.energy =[]

        for i in range(int(self.data["sizeBoard"])):
            self.tweakSolution(self.current)

    #изменение решения
    def tweakSolution(self, member):
        x = rm.randint(0, self.data["sizeBoard"] - 1)
        y = rm.randint(0, self.data["sizeBoard"] - 1)
        while y == x:
            y = rm.randint(0, self.data["sizeBoard"] - 1)
        member["solution"][x], member["solution"][y] = member["solution"][y], member["solution"][x]

    def checkDiag(self, x1, y1, x2, y2):

        return int(abs(x1 - x2) == abs(y1 - y2))

    #оценка решения
    #подсчет кол-ва конфликтов
    def computeEnergy(self, member):

        conf = 0
        for x1, y1 in enumerate(member["solution"]):
            for x2, y2 in enumerate(member["solution"]):
                if x1 != x2:
                    conf += self.checkDiag(x1, y1, x2, y2)

        member["energy"] = conf

        #копирование структуры src типа memberType в cструктуру dest
    def copySolution(self, dest, src):
        dest["solution"] = src["solution"].copy()
        dest["energy"] = src["energy"]

    def process(self):
        timer = 0
        solution = False
        self.computeEnergy(self.current)

        best = {
            "solution": [i for i in range(int(self.data["sizeBoard"]))],
            "energy": 100
        }

        working = {
            "solution": self.current["solution"],
            "energy": self.current["energy"]
        }

        while self.data["startTemp"] > self.data["endTemp"]:
            #Изменены решения случайным образом
            for step in range(int(self.data["stepRepChange"])):
                useNew = False

                #изменяем рабочее решение
                self.tweakSolution(working)
                #считаем конфликты
                self.computeEnergy(working)

                if working["energy"] <= self.current["energy"]:
                    useNew = True
                else:
                    test = rm.random()
                    delta = working["energy"] - self.current["energy"]
                    calc = (math.e ** (-delta / self.data["startTemp"]))
                    if calc > test:
                        useNew = True

                if useNew:
                    useNew = False
                    self.copySolution(self.current, working)
                    if self.current["energy"] < best["energy"]:
                        self.copySolution(best, self.current)
                        solution = True
                    else:
                        self.copySolution(working,self.current)

            timer += 1
            self.temp.append(self.data["startTemp"])
            self.energy.append(best["energy"])
            #print(timer, self.data["startTemp"], best["energy"])
            self.data["startTemp"] *= self.data["alpha"]

        if solution:
            print(best["energy"])
            return (best["solution"], self.temp, self.energy)
        return None

