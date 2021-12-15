from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Problem0012.txt") as f:
        initial = [int(x) for x in f.readline().split(',')]
        fishes = {index: len(list(filter(lambda x: x == index, initial))) for index in range(0, 9)}
        for i in range(0, 256):
            newFishes = fishes[0]
            for i in range(0, 8):
                fishes[i] = fishes[i + 1]
            fishes[8] = newFishes
            fishes[6] += newFishes

    return sum(fishes.values())

run()
