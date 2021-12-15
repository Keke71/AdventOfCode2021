from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Problem0015.txt") as f:
        lines = [line.rstrip() for line in f]
        output = [line.split(' | ')[1].split() for line in lines]

        count = len(list(filter(lambda x: len(x) >= 2 and len(x) <= 4 or len(x) == 7, [y for line in output for y in line])))

    return count

run()
