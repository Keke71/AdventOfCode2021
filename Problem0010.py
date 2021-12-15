from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Problem0010.txt") as f:
        lines = list([int(x) for x in textLine.replace(' -> ', ',').split(',')] for textLine in f.readlines())
        width = max(max(lines, key=lambda x: max(x[0], x[2]))) + 1
        height = max(max(lines, key=lambda x: max(x[1], x[3]))) + 1
        matrix = [[0] * width for _ in range(height)]

        for line in lines:
            if line[0] == line[2]:
                for i in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                    matrix[i][line[0]] += 1
            elif line[1] == line[3]:
                for i in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                    matrix[line[1]][i] += 1
            else:
                dx = 0 if line[0] == line[2] else (1 if line[0] < line[2] else -1)
                dy = 0 if line[1] == line[3] else (1 if line[1] < line[3] else -1)
                for i in range(0, abs(line[2] - line[0]) + 1):
                    matrix[line[1] + i * dy][line[0] + i * dx] += 1


    return len(list(filter(lambda x: x > 1, [y for line in matrix for y in line])))

run()
