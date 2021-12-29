from helpers.problemrunner import run_problem
from itertools import groupby
from operator import itemgetter
import time


@run_problem
def run():
    with open("Problem0027.txt") as f:
        lines = list(line.rstrip() for line in f)
    template = lines[0]
    rules = { y[0]:y[1] for y in [line.split(' -> ') for line in lines[2:]] }

    for j in range(1, 11):
        newTemplate = ''
        for i in range(len(template) - 1):
            pair = template[i:i+2]
            newTemplate += pair[0] + rules[pair]
        newTemplate += template[-1]
        template = newTemplate

    counts = {key: sum(x[1] for x in value) for (key, value) in groupby(sorted((c, 1) for c in template), key=itemgetter(0))}
    return max(counts.values()) - min(counts.values())


run()
