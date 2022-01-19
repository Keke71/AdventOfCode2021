from helpers.problemrunner import run_problem
from math import sqrt, ceil


@run_problem
def run():
    with open("Problem0034.txt") as f:
        target_area = f.readline().lstrip('target area: x=')
        points = target_area.split(', y=')
        x_coords = points[0].split('..')
        y_coords = points[1].split('..')
        target = Target(x_coords, y_coords)
        y0_min = target.bottom
        y0_max = -target.bottom
        # Sum of all x steps must be at least target.left
        # x0_min*(x0_min + 1) / 2 >= target.left
        x0_min = ceil((-1 + sqrt(1 + 8 * target.left)) / 2)
        # Every x0 above half distance to the right edge of the target will run beyond target in the second step
        x0_max = ceil(target.right / 2)

        count = 0
        for y in range(y0_min, y0_max + 1):
            for x in range(x0_min, x0_max + 1):
                shot = Shot(x, y, target)
                if shot.hits_target():
                    count += 1

        # Direct shots on target were not considered yet
        count += target.size()

        return count


class Target():
    def __init__(self, x_coords, y_coords):
        self.left = int(x_coords[0])
        self.right = int(x_coords[1])
        self.top = int(y_coords[1])
        self.bottom = int(y_coords[0])


    def size(self):
        return (self.right - self.left + 1) * (self.top - self.bottom + 1)


class Shot():
    def __init__(self, initial_speed_x, initial_speed_y, target):
        self.speed_x = initial_speed_x
        self.speed_y = initial_speed_y
        self.target = target
        self.x = 0
        self.y = 0

    
    def hits_target(self):
        while self.next():
            if self.in_target():
                return True
        return False


    def next(self):
        self.x = self.x + self.speed_x
        self.y = self.y + self.speed_y
        self.speed_x = max(0, self.speed_x - 1)
        self.speed_y -= 1
        
        return self.x <= self.target.right and self.y >= self.target.bottom


    def in_target(self):
        return self.target.left <= self.x <= self.target.right and self.target.bottom <= self.y <= self.target.top


run()
