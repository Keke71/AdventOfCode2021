from helpers.problemrunner import run_problem
from functools import reduce


@run_problem
def run():
    with open("Problem0020.txt") as f:
        lines = list([x for x in textLine.strip()] for textLine in f)

    parser = NavLineParser()

    return parser.getScore(lines)


class NavLineParser:
    score = []
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']


    def getScore(self, lines):
        for line in lines:
            self.parseLine(line)

        return sorted(self.score)[len(self.score) // 2]


    def parseLine(self, line):
        tokens = []
        for x in line:
            if x in self.opening:
                tokens.append(self.opening.index(x))
            else:
                index = tokens.pop()
                if x != self.closing[index]:
                    return

        self.score.append(reduce(lambda a, b: a * 5 + b + 1, reversed(tokens), 0))


run()
