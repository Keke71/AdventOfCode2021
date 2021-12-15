from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Problem0014.txt") as f:
        positions = [int(x) for x in f.readline().split(',')]
        maxPosition = max(positions)
        minCosts = maxPosition * len(positions) * len(positions) // 2
        for i in range(0, maxPosition + 1):
            minCosts = min(minCosts, sum([abs(pos - i) * (abs(pos - i) + 1) // 2 for pos in positions]))

    return minCosts

run()
