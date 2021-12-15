from helpers.problemrunner import run_problem
from functools import reduce


@run_problem
def run():
    with open("Problem0004.txt") as f:
        lines = [(line[0], int(line[1]))
                 for line in (l.split() for l in f.readlines())]
        aim = 0
        depth = 0
        position = 0
        for line in lines:
            if line[0] == "down":
                aim += line[1]
            elif line[0] == "up":
                aim -= line[1]
            elif line[0] == "forward":
                position += line[1]
                depth += aim * line[1]

        return position * depth


run()
