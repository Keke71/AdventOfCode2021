from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Problem0017.txt") as f:
        matrix = list([int(x) for x in textLine.strip()] for textLine in f)
        width = len(matrix[0])
        height = len(matrix)
        sum = 0
        for y in range(height):
            for x in range(width):
                current = matrix[y][x]
                left = matrix[y][x-1] if x > 0 else 10
                top = matrix[y-1][x] if y > 0 else 10
                right = matrix[y][x+1] if x < width - 1 else 10
                bottom = matrix[y+1][x] if y < height - 1  else 10
                if current < left and current < top and current < right and current < bottom:
                    sum += current + 1

    return sum

run()
