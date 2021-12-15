from helpers.problemrunner import run_problem

matrixSize = 5

@run_problem
def run():
    with open("Problem0008.txt") as f:
        lines = list(filter(None, (line.rstrip() for line in f)))
        matrixes = list([])
        drawnNumbers = [int(number) for number in lines[0].split(',')]
        index = 1
        while index < len(lines):
            if index % matrixSize == 1:
                matrixes.append([])
            matrixes[(index - 1) // matrixSize].extend([int(number) for number in lines[index].split()])
            index += 1

        isOpen = [True] * len(matrixes)
        for drawn in drawnNumbers:
            for i in range(0, len(matrixes)):
                if not isOpen[i]:
                    continue
                matrixes[i] = list(map(lambda x: None if x == drawn else x, matrixes[i]))
                if isFinished(matrixes[i]):
                    if sum(isOpen) > 1:
                        isOpen[i] = False
                    else:
                        return drawn * sum(x for x in matrixes[i] if x != None)


def isFinished(matrix):
    for i in range(0, matrixSize):
        row = list(filter(lambda x: x != None, matrix[i * matrixSize:i * matrixSize + matrixSize]))
        if len(row) == 0:
            return True
        column = list(filter(lambda x: x != None, matrix[i::matrixSize]))
        if len(column) == 0:
            return True
    return False
    

run()
