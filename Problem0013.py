from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Problem0013.txt") as f:
        positions = [int(x) for x in f.readline().split(',')]
        maxPosition = max(positions)
        minCosts = maxPosition * len(positions)
        for i in range(0, maxPosition + 1):
            minCosts = min(minCosts, sum([abs(pos - i) for pos in positions]))

    return minCosts

run()
