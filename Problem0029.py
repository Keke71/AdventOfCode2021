from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Problem0029.txt") as f:
        matrix = list([int(x) for x in textLine.strip()] for textLine in f)

    return Cave().find_path(matrix)

class Cave():

    def find_path(self, matrix):
        width = len(matrix[0])
        height = len(matrix)
        self.maximum_sum = (width + height) * 9
        self.matrix = [[Chiton(matrix[y][x]) for x in range(width)] * width for y in range(height)]
        
        return self.get_minimum_risk_above(width - 1, height - 1)


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
