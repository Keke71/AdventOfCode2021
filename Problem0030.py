from helpers.problemrunner import run_problem
import sys


@run_problem
def run():
    sys.setrecursionlimit(10000)
    with open("Problem0030.txt") as f:
        folded_matrix = list([int(x) for x in textLine.strip()] for textLine in f)
    height = len(folded_matrix)
    temp_matrix = []
    for y in range(height):
        temp_matrix.append([(x - 1 + i) % 9 + 1 for i in range(5) for x in folded_matrix[y]])
    matrix = []
    for i in range(5):
        for y in range(height):
            matrix.append([(x - 1 + i) % 9 + 1 for x in temp_matrix[y]])

    return Cave().find_path(matrix)

class Cave():

    def find_path(self, matrix):
        self.width = len(matrix[0])
        self.height = len(matrix)
        self.maximum_sum = (self.width + self.height) * 9
        self.matrix = [[Chiton(matrix[y][x]) for x in range(self.width)] * self.width for y in range(self.height)]
        
        return self.get_minimum_risk_above(self.width - 1, self.height - 1)


    def get_minimum_risk_above(self, x, y):
        if x == 0 and y == 0:
            return 0

        chiton = self.matrix[y][x]
        if chiton.minimum_risk_above != 0:
            return chiton.minimum_risk_above

        risk_left = self.get_minimum_risk_above(x - 1, y) if x > 0 else self.maximum_sum
        risk_top = self.get_minimum_risk_above(x, y - 1) if y > 0 else self.maximum_sum
        chiton.minimum_risk_above = chiton.risk + min(risk_left, risk_top)

        return chiton.minimum_risk_above


class Chiton():
    def __init__(self, risk):
        self.risk = risk
        self.minimum_risk_above = 0


run()
