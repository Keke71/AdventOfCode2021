from helpers.problemrunner import run_problem


@run_problem
def run():
    count = 0
    with open("Problem0002.txt") as f:
        lines = [int(l) for l in f.readlines()]
        for i in range(3, len(lines)):
            if sum(lines[i-2:i+1]) > sum(lines[i-3:i]):
                count += 1

    return count


run()
