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
        self.matrix = matrix
        self.known_minimum_risks = [[0] * width for _ in range(height)]
        
        return self.get_minimum_risk_above(width - 1, height - 1)


    def get_minimum_risk_above(self, x, y):
        if x == 0 and y == 0:
            return 0

        if self.known_minimum_risks[y][x] != 0:
            return self.known_minimum_risks[y][x]

        risk_left = self.get_minimum_risk_above(x - 1, y) if x > 0 else self.maximum_sum
        risk_top = self.get_minimum_risk_above(x, y - 1) if y > 0 else self.maximum_sum
        risk = self.matrix[y][x] + min(risk_left, risk_top)
        self.known_minimum_risks[y][x] = risk

        return risk


run()
