from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Problem0021.txt") as f:
        matrix = list([int(x) for x in textLine.strip()] for textLine in f)

    octopuses = Octopuses(matrix)
    for _ in range(0, 100):
        octopuses.IncrementAll()
        while octopuses.CanFlash():
            octopuses.Flash()
        octopuses.ResetFlashed()

    return octopuses.flashed


class Octopuses:
    def __init__(self, matrix):
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)
        self.flashed = 0

    def IncrementAll(self):
        for y in range(self.height):
            for x in range(self.width):
                self.matrix[y][x] += 1

    def CanFlash(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x] > 9:
                    return True
        return False

    def Flash(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x] > 9:
                    self.IncrementSurrounding(x, y)
                    self.matrix[y][x] = -1
                    self.flashed += 1

    def IncrementSurrounding(self, x, y):
        self.Increment(x-1, y-1)
        self.Increment(x, y-1)
        self.Increment(x+1, y-1)
        self.Increment(x+1, y)
        self.Increment(x+1, y+1)
        self.Increment(x, y+1)
        self.Increment(x-1, y+1)
        self.Increment(x-1, y)

    def Increment(self, x, y):
        if x >= 0 and x < self.width and y >= 0 and y < self.width and self.matrix[y][x] != -1:
            self.matrix[y][x] += 1

    def ResetFlashed(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x] == -1:
                    self.matrix[y][x] = 0

run()
