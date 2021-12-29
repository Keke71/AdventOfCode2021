from helpers.problemrunner import run_problem
from math import sqrt, ceil


@run_problem
def run():
    with open("Problem0035.txt") as f:
        numbers = list(line.rstrip() for line in f)
        sum = ''
        for n in numbers:
            number = SnailfishNumber(n).number
            if len(sum) == 0:
                sum = number
            else:
                sum = f'[{sum}, {number}]'
        
        return sum


class SnailfishNumber():
    def __init__(self, number):
        self.number = number
        self.position = 0
        self.number_stack = []
        self.level = 0
        self.reduce()

        pass

    
    def reduce(self):
        self.read_number()


    def read_number(self):
        if self.check('['):
            self.level += 1
            self.read('[')
            self.read_number()
            self.read(',')
            self.read_number()
            self.read(']')
            right = self.number_stack.pop()
            left = self.number_stack.pop()
            self.number_stack.append((left, right))

            # if self.level == 5:
            #     self.explode()

            self.level -= 1
        else:
            self.literal()


    def literal(self):
        self.number_stack.append(int(self.number[self.position]))
        self.position += 1


    def explode(self):
        last_tuple = self.number_stack.pop()
        if len(self.number_stack) > 0:
            previous = self.number_stack.pop()
            self.number_stack.append(previous + last_tuple[0])
        if self.check(','):
            self.read(',')
            self.read_number()
            next = self.number_stack.pop()
            self.number_stack.append(next + right)


    def check(self, character):
        return self.number[self.position] == character


    def read(self, characters):
        # self.number_stack.append(characters)
        self.position += len(characters)


run()
