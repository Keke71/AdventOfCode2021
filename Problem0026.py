from helpers.problemrunner import run_problem
from itertools import takewhile, dropwhile


@run_problem
def run():
    with open("Problem0026.txt") as f:
        lines = list(line.rstrip() for line in f)
    coordinates = [(int(line[0]), int(line[1])) for line in (l.split(',') for l in takewhile(lambda x: x != '', lines))]
    foldInstructions = list(dropwhile(lambda x: x != '', lines))[1:]
    paper = TransparentPaper(coordinates)
    for instruction in foldInstructions:
        paper.foldMatrix(instruction)

    paper.print()


class TransparentPaper:
    def __init__(self, coordinates):
        self.width = max(coordinates, key=lambda x: x[0])[0] + 1
        self.height = max(coordinates, key=lambda x: x[1])[1] + 1
        self.matrix = [[0] * self.width for _ in range(self.height)]
        for coordinate in coordinates:
            self.matrix[coordinate[1]][coordinate[0]] = 1


    def foldMatrix(self, foldInstruction):
        direction = foldInstruction.lstrip('fold along ').split('=')[0]
        if direction == 'x':
            return self.foldHorizontal()
        else:
            return self.foldVertical()


    def foldHorizontal(self):
        newWidth = self.width // 2
        foldedMatrix = [[0] * newWidth for _ in range(self.height)]
        for y in range(self.height):
            for x in range(newWidth):
                foldedMatrix[y][x] = self.matrix[y][x] | self.matrix[y][self.width - x - 1]
        self.updateMatrix(foldedMatrix)


    def foldVertical(self):
        newHeight = self.height // 2
        foldedMatrix = [[0] * self.width for _ in range(newHeight)]
        for y in range(newHeight):
            for x in range(self.width):
                foldedMatrix[y][x] = self.matrix[y][x] | self.matrix[self.height - y - 1][x]
        self.updateMatrix(foldedMatrix)


    def updateMatrix(self, matrix):
        self.matrix = matrix
        self.width = len(matrix[0])
        self.height = len(matrix)


    def print(self):
        for line in self.matrix:
            for c in line:
                print('#' if c==1 else ' ', end='')
            print()



run()
