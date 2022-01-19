from helpers.problemrunner import run_problem


@run_problem
def run():
    # Upwards decelaration is equal to downwards accelaration -> way up is equal to way down
    # -> Probe will always hit y=0 on the way down
    # -> Maximum allowed step on the way down at y=0 is 148, as -148 is the lower bound of the target area
    # -> Maximum allowed initial speed in y-direction is 147
    # -> highest point is the sum of [1..147] = 147*148/2 = 10878

    with open("Problem0034.txt") as f:
        target_area = f.readline().lstrip('target area: x=')
        points = target_area.split(', y=')
        y0_max = -int(points[1].split('..')[0]) - 1
    
    return y0_max * (y0_max + 1) / 2


run()
