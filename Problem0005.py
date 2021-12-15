from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Problem0005.txt") as f:
        lines = [list(line) for line in f.readlines()]
        numberLength = len(lines[0])
        halfCount = len(lines) / 2
        gammaRate = []
        epsilonRate = []
        for i in range(numberLength - 1):
            count = sum(int(line[i]) for line in lines)
            gammaRate.append('1' if count > halfCount else '0')
            epsilonRate.append('0' if count > halfCount else '1')

        return int(''.join(gammaRate), 2) * int(''.join(epsilonRate), 2)


run()
