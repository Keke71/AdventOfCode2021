from helpers.problemrunner import run_problem
from math import sqrt, ceil


@run_problem
def run():
    with open("Problem0035.txt") as f:
        numbers = list(line.rstrip() for line in f)
        sum = ''
        for n in numbers:
            number = SnailfishNumber(n)
            number.print()

            # if len(sum) == 0:
            #     sum = number
            # else:
            #     sum = f'[{sum}, {number}]'
        
        # return sum


class SnailfishNumber():
    def __init__(self, number):
        self.number = number
        self.position = 0
        self.current_level = 0
        self.parse()


    def parse(self):
        self.root = self.read_element()


    def read_element(self):
        if self.read('['):
            return self.read_pair()
        else:
            return self.read_literal()


    def read_pair(self):
        self.current_level += 1
        left = self.read_element()
        self.read(',')
        right = self.read_element()
        self.read(']')
        self.current_level -= 1

        return Pair(left, right, self.current_level)


    def read_literal(self):
        number = self.number[self.position]
        self.position += 1
        return Literal(number, self.current_level)


    def read(self, characters):
        length = len(characters)
        if self.number[self.position:self.position + length] == characters:
            self.position += length
            return True
        return False


    def print(self):
        self.root.print()
        print()


class Element():
    def __init__(self, level):
        self.level = level


class Literal(Element):
    def __init__(self, value, level):
        super().__init__(level)
        self.value = value


    def print(self):
        print(f'{self.value}', end='')


class Pair(Element):
    def __init__(self, left, right, level):
        super().__init__(level)
        self.left = left
        self.right = right


    def print(self):
        print(f'_{self.level}_', end='')
        print('[', end='')
        self.left.print()
        print(',', end='')
        self.right.print()
        print(']', end='')


run()
