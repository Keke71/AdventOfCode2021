from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Problem0018.txt") as f:
        matrix = list([int(x) for x in textLine.strip()] for textLine in f)

    width = len(matrix[0])
    height = len(matrix)
    lowPoints = []
    basins = []
    for y in range(height):
        for x in range(width):
            current = matrix[y][x]
            left = matrix[y][x-1] if x > 0 else 10
            top = matrix[y-1][x] if y > 0 else 10
            right = matrix[y][x+1] if x < width - 1 else 10
            bottom = matrix[y+1][x] if y < height - 1  else 10
            if current < left and current < top and current < right and current < bottom:
                lowPoints.append((x,y))
    
    for point in lowPoints:
        basins.append(countNeighboursForPoint(matrix, point, width, height))
    basins.sort(reverse=True)

    return basins[0] * basins[1] * basins[2]


def countNeighboursForPoint(matrix, point, width, height):
    if point == None:
        return 0
    return countNeighbours(matrix, point[0], point[1], width, height)

def countNeighbours(matrix, x, y, width, height):
    ret = 0
    ret += mark(matrix, x, y)
    left = (x-1, y) if x > 0 and matrix[y][x-1] < 9 else None
    top = (x, y-1) if y > 0 and matrix[y-1][x] < 9 else None
    right = (x+1, y) if x < width - 1 and matrix[y][x+1] < 9 else None
    bottom = (x, y+1) if y < height - 1 and matrix[y+1][x] < 9 else None
    ret += markPoint(matrix, left)
    ret += markPoint(matrix, top)
    ret += markPoint(matrix, right)
    ret += markPoint(matrix, bottom)
    ret += countNeighboursForPoint(matrix, left, width, height)
    ret += countNeighboursForPoint(matrix, top, width, height)
    ret += countNeighboursForPoint(matrix, right, width, height)
    ret += countNeighboursForPoint(matrix, bottom, width, height)

    return ret


def markPoint(matrix, point):
    if point == None:
        return 0
    return mark(matrix, point[0], point[1])


def mark(matrix, x, y):
    if matrix[y][x] != 10:
        matrix[y][x] = 10
        return 1
    return 0




run()
