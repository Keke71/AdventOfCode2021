from helpers.problemrunner import run_problem
from helpers.dicthelpers import increase_or_update


@run_problem
def run():
    with open("Problem0028.txt") as f:
        lines = list(line.rstrip() for line in f)
    template = lines[0]
    rules = { y[0]:y[1] for y in [line.split(' -> ') for line in lines[2:]] }
    letterCounts = { letter: 0 for letter in set(rules.values()) }
    for letter in template:
        letterCounts[letter] += 1
    pairCounts = { template[i:i+2]: 1 for i in range(len(template) - 1) }

    for _ in range(1, 41):
        newPairs = {}
        removePairs = {}
        for (pair, count) in filter(lambda x: x[1] > 0, pairCounts.items()):
            removePairs[pair] = count
            newPair1 = pair[0] + rules[pair]
            newPair2 = rules[pair] + pair[1]
            letterCounts[rules[pair]] += count
            increase_or_update(newPairs, newPair1, count)
            increase_or_update(newPairs, newPair2, count)

        for (pair, count) in removePairs.items():
            pairCounts[pair] -= count

        for (pair, count) in newPairs.items():
            increase_or_update(pairCounts, pair, count)

    return max(letterCounts.values()) - min(letterCounts.values())


run()
