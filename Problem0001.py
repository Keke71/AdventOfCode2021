from helpers.problemrunner import run_problem


@run_problem
def run():
    count = 0
    with open("Problem0001.txt") as f:
        lines = [int(l) for l in f.readlines()]
        for i in range(1, len(lines)):
            if lines[i] > lines[i-1]:
                count += 1
    return count


run()
