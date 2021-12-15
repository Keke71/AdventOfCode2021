from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Problem0009.txt") as f:
        lines = list([int(x) for x in textLine.replace(' -> ', ',').split(',')] for textLine in f.readlines())
        lines = list(filter(lambda x: x[0] == x[2] or x[1] == x[3], lines))
        width = max(max(lines, key=lambda x: max(x[0], x[2]))) + 1
        height = max(max(lines, key=lambda x: max(x[1], x[3]))) + 1
        matrix = [[0] * width for _ in range(height)]

        for line in lines:
            if line[0] == line[2]:
                for i in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                    matrix[i][line[0]] += 1
            else:
                for i in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                    matrix[line[1]][i] += 1

    return len(list(filter(lambda x: x > 1, [y for line in matrix for y in line])))

run()
