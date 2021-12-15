from helpers.problemrunner import run_problem

@run_problem
def run():
    with open("Problem0016.txt") as f:
        numbers = {
            '012456': '0',
            '25': '1',
            '02346': '2',
            '02356': '3',
            '1235': '4',
            '01356': '5',
            '013456': '6',
            '025': '7',
            '0123456': '8',
            '012356': '9'
        }
        lines = [line.rstrip() for line in f]
        sum = 0
        for line in lines:
            patterns = line.split(' | ')[0].split()
            outputs = line.split(' | ')[1].split()
            positions = {}
            connections = {}
            a1 = list(list(filter(lambda x: len(x) == 2, patterns))[0])
            a7 = list(list(filter(lambda x: len(x) == 3, patterns))[0])
            connections[0] = [x for x in a7 if x not in a1][0]
            positions[connections[0]] = 0
            a6 = list(filter(lambda x: len(x) == 6 and a1[0] in x and not a1[1] in x, patterns))
            if len(a6) > 0:
                positions[a1[0]] = 5
                positions[a1[1]] = 2
                connections[5] = a1[0]
                connections[2] = a1[1]
            else:
                positions[a1[0]] = 2
                positions[a1[1]] = 5
                connections[2] = a1[0]
                connections[5] = a1[1]
            a4 = list(list(filter(lambda x: len(x) == 4, patterns))[0])
            a4 = [x for x in a4 if x not in a1]
            a0 = list(filter(lambda x: len(x) == 6 and a4[0] in x and not a4[1] in x, patterns))
            if len(a0) > 0:
                positions[a4[0]] = 1
                positions[a4[1]] = 3
                connections[1] = a4[0]
                connections[3] = a4[1]
            else:
                positions[a4[0]] = 3
                positions[a4[1]] = 1
                connections[3] = a4[0]
                connections[1] = a4[1]
            a5 = list(list(filter(lambda x: len(x) == 5
                and connections[0] in x
                and connections[1] in x
                and connections[3] in x
                and connections[5] in x,
                patterns))[0])
            a5 = [x for x in a5 if x != connections[0]
                and x != connections[1]
                and x != connections[3]
                and x != connections[5]]
            positions[a5[0]] = 6
            connections[6] = a5[0]
            a8 = list(list(filter(lambda x: len(x) == 7, patterns))[0])
            a8 = [x for x in a8 if not x in positions.keys()]
            positions[a8[0]] = 4

            number = ''
            for output in outputs:
                signal = ''
                for c in output:
                    signal += str(positions[c])
                number += numbers[''.join(sorted(signal))]
            sum += int(number)

    return sum

        #   0
        # 1   2
        #   3
        # 4   5
        #   6
        # 
        # 2-digits -> [a1, a2] (1)
        # 3-digits -> [a1, a2, a3] -> a3 = 0 (7)
        # 6-digits where either a1 or a2 are contained -> contained (c1) = 5, not contained (c2) = 2 (6)
        # 4-digits -> [a1, a2, a6, a7] (4)
        # 6-digits where either a6 or a7 are contained -> contained (c3) = 1, not contained (c4) = 3 (0)
        # 5-digit -> [a3, c3, c4, c1, a4] -> a4 = 6, a5 = 4 (5)

    return count

run()
