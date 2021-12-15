from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Problem0019.txt") as f:
        lines = list([x for x in textLine.strip()] for textLine in f)

    parser = NavLineParser()

    return parser.getScore(lines)


class NavLineParser:
    score = 0
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    def getScore(self, lines):
        for line in lines:
            self.parseLine(line)

        return self.score

    def parseLine(self, line):
        tokens = []
        for x in line:
            if x in self.opening:
                tokens.append(self.opening.index(x))
            else:
                index = tokens.pop()
                if x != self.closing[index]:
                    self.score += self.scores[x]
                    return


run()
