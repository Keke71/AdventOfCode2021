from helpers.problemrunner import run_problem
from helpers.dicthelpers import increase_or_update


@run_problem
def run():
    with open("Problem0028.txt") as f:
        lines = list(line.rstrip() for line in f)
    template = lines[0]
    rules = { y[0]:y[1] for y in [line.split(' -> ') for line in lines[2:]] }
    letterCount = { letter: 0 for letter in set(rules.values()) }
    for letter in template:
        letterCount[letter] += 1
    counts = { template[i:i+2]: 1 for i in range(len(template) - 1) }

    for _ in range(1, 41):
        newPairs = {}
        removePairs = {}
        for (pair, count) in filter(lambda x: x[1] > 0, counts.items()):
            removePairs[pair] = count
            newPair1 = pair[0] + rules[pair]
            newPair2 = rules[pair] + pair[1]
            letterCount[rules[pair]] += count
            increase_or_update(newPairs, newPair1, count)
            increase_or_update(newPairs, newPair2, count)

        for (pair, count) in removePairs.items():
            counts[pair] -= count

        for (pair, count) in newPairs.items():
            increase_or_update(counts, pair, count)

    return max(letterCount.values()) - min(letterCount.values())


run()
