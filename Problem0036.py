from helpers.problemrunner import run_problem
from math import floor, ceil


@run_problem
def run():
    with open("Problem0036.txt") as f:
        numbers = list(line.rstrip() for line in f)
        max_magnitude = 0
        for i in range(len(numbers)):
            for n in numbers[:i] + numbers[i+1:]:
                first = SnailfishNumber(numbers[i])
                second = SnailfishNumber(n)
                first.add(second)
                max_magnitude = max(max_magnitude, first.magnitude())
                
        return max_magnitude


class SnailfishNumber():
    def __init__(self, number):
        self.number = number
        self.position = 0
        self.current_level = 0
        self.literals = []
        self.parse()


    def parse(self):
        self.read_element()
        self.reduce()


    def read_element(self):
        if self.read('['):
            self.read_pair()
        else:
            self.literals.append(self.read_literal())


    def read_pair(self):
        self.current_level += 1
        self.read_element()
        self.read(',')
        self.read_element()
        self.read(']')
        self.current_level -= 1


    def read_literal(self):
        number = int(self.number[self.position])
        self.position += 1
        return Literal(number, self.current_level)


    def reduce(self):
        done = False
        while not done:
            while self.explode():
                pass
            if not self.split():
                done = True


    def explode(self):
        for i in range(len(self.literals)):
            if self.literals[i].level == 5 and self.literals[i+1].level == 5:
                if i > 0:
                    self.literals[i-1].value += self.literals[i].value
                if i < len(self.literals) - 2:
                    self.literals[i+2].value += self.literals[i+1].value
                self.literals[i].value = 0
                self.literals[i].level -= 1
                self.literals.remove(self.literals[i+1])
                return True
        return False


    def split(self):
        for i in range(len(self.literals)):
            if self.literals[i].value >= 10:
                self.literals[i].level += 1
                self.literals.insert(i+1, Literal(ceil(self.literals[i].value / 2), self.literals[i].level))
                self.literals[i].value = floor(self.literals[i].value / 2)
                return True

        return False

    
    def add(self, other):
        self.literals += other.literals
        for literal in self.literals:
            literal.level += 1
        self.reduce()


    def magnitude(self):
        max_level = max(map(lambda x: x.level, self.literals))
        while len(self.literals) > 1:
            i = 0
            while i < len(self.literals) - 1:
                if self.literals[i].level == max_level and self.literals[i+1].level == max_level:
                    self.literals[i].value = 3 * self.literals[i].value + 2 * self.literals[i + 1].value
                    self.literals[i].level -= 1
                    self.literals.remove(self.literals[i+1])
                i += 1
            max_level -= 1

        return self.literals[0].value


    def read(self, characters):
        length = len(characters)
        if self.number[self.position:self.position + length] == characters:
            self.position += length
            return True
        return False


    def print(self):
        for literal in self.literals:
            print(f'{literal.value}, Level={literal.level}')


class Literal():
    def __init__(self, value, level):
        self.value = value
        self.level = level


run()
