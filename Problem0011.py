from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Problem0011.txt") as f:
        initial = [int(x) for x in f.readline().split(',')]
        fishes = {}
        for i in range(0, 9):
            fishes[i] = len(list(filter(lambda x: x == i, initial)))
        for i in range(0, 80):
            newFishes = fishes[0]
            for i in range(0, 8):
                fishes[i] = fishes[i + 1]
            fishes[8] = newFishes
            fishes[6] += newFishes

    return sum(fishes.values())

run()
