from helpers.problemrunner import run_problem


@run_problem
def run():
    # Way up: n*(n+1)/2
    # Way down: n*(n+1)/2
    # -> Probe will always pass y=0 on the way down
    # -> Maximum speed on the way down at y=0 is 148, as -148 is the lower bound of the target area
    # -> Initial speed in y-direction is 147
    # -> highest point is the sum of [1..147] = 147*148/2 = 10878
    pass

run()
