from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Problem0030.txt") as f:
        folded_matrix = list([int(x) for x in textLine.strip()] for textLine in f)
    height = len(folded_matrix)
    temp_matrix = []
    for y in range(height):
        temp_matrix.append([(x - 1 + i) % 9 + 1 for i in range(5) for x in folded_matrix[y]])
    matrix = []
    for i in range(5):
        for y in range(height):
            matrix.append([(x - 1 + i) % 9 + 1 for x in temp_matrix[y]])

    return Cave().find_path(matrix)

class Cave():

    def find_path(self, matrix):
        self.width = len(matrix[0])
        self.height = len(matrix)
        self.maximum_sum = (self.width + self.height) * 9
        self.matrix = [[Chiton(x, y, matrix[y][x], self.maximum_sum) for x in range(self.width)] for y in range(self.height)]
        self.matrix[0][0].distance = 0
        self.open_list = set([self.matrix[0][0]])
        self.closed_list = set()

        while len(self.open_list) > 0:
            q = sorted(self.open_list, key=lambda x: x.distance)[0]
            self.open_list.remove(q)
            self.closed_list.add(q)
            self.add_to_open_list(q.x + 1, q.y)
            self.add_to_open_list(q.x, q.y + 1)
            self.add_to_open_list(q.x - 1, q.y)
            self.add_to_open_list(q.x, q.y - 1)
            self.update_distance(q, q.x + 1, q.y)
            self.update_distance(q, q.x, q.y + 1)
            self.update_distance(q, q.x - 1, q.y)
            self.update_distance(q, q.x, q.y - 1)

        return self.matrix[self.height - 1][self.width - 1].distance
    
    def add_to_open_list(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            chiton = self.matrix[y][x]
            if chiton not in self.closed_list and chiton not in self.closed_list:
                self.open_list.add(chiton)

    def update_distance(self, chiton, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            neighbor = self.matrix[y][x]
            if neighbor in self.open_list:
                dist = chiton.distance + neighbor.risk
                if dist < neighbor.distance:
                    neighbor.distance = dist
                    neighbor.parent = chiton


class Chiton():
    def __init__(self, x, y, risk, maximum):
        self.x = x
        self.y = y
        self.risk = risk
        self.parent = None
        self.distance = maximum


run()
