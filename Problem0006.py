from helpers.problemrunner import run_problem


bitCriteria = ['0', '1']


@run_problem
def run():
    with open("Problem0006.txt") as f:
        lines = [list(line) for line in f.readlines()]
        oxygen = getRating(lines, 1)
        scrubber = getRating(lines, 0)

        return int(''.join(oxygen), 2) * int(''.join(scrubber), 2)


def getRating(lines, bitCriteriaIndex):
    remainingLines = lines.copy()
    i = 0
    while len(remainingLines) > 1:
        halfCount = len(remainingLines) / 2
        count = sum(int(line[i]) for line in remainingLines)
        mostCommonBit = bitCriteria[bitCriteriaIndex] if count >= halfCount else bitCriteria[(
            bitCriteriaIndex + 1) % 2]
        remainingLines = list(
            filter(lambda x: x[i] == mostCommonBit, remainingLines))
        i += 1

    return remainingLines[0]


run()
