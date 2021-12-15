from helpers.problemrunner import run_problem
from itertools import groupby
from operator import itemgetter


@run_problem
def run():
    with open("Problem0003.txt") as f:
        lines = sorted((line[0], int(line[1])) for line in (l.split() for l in f.readlines()))
        d = {key: sum(x[1] for x in value) for (key, value) in groupby(lines, key=itemgetter(0))}
        return d["forward"] * (d["down"] - d["up"])


run()
