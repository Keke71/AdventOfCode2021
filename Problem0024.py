from helpers.problemrunner import run_problem


@run_problem
def run():
    with open("Problem0024.txt") as f:
        lines = list(line.rstrip().split('-') for line in f)
    caveSystem = CaveSystem(lines)

    return caveSystem.CountPaths()

class CaveSystem:
    def __init__(self, connections):
        self.caves = []
        self.pathCount = 0
        for connection in connections:
            cave1 = self.GetOrCreate(connection[0])
            cave2 = self.GetOrCreate(connection[1])
            cave1.ConnectTo(cave2)


    def GetOrCreate(self, name):
        cave = next((x for x in self.caves if x.name == name), None)
        if cave == None:
            cave = Cave(name)
            self.caves.append(cave)

        return cave


    def CountPaths(self):
        self.FindPath(next(x for x in self.caves if x.isStartCave))
        return self.pathCount


    def FindPath(self, cave):
        if cave.isEndCave:
            self.pathCount += 1
            return
        cave.Visit()
        for connectedCave in cave.connections:
            if connectedCave.CanBeVisited() or connectedCave.visited == 1 and all(map(lambda x: x.visited <= 1, self.caves)):
                self.FindPath(connectedCave)
        cave.Unvisit()


class Cave:
    def __init__(self, name):
        self.name = name
        self.isStartCave = name == "start"
        self.visited = 0
        self.isEndCave = name == "end"
        self.isBigCave = name[0].isupper()
        self.connections = []

    def ConnectTo(self, cave):
        self.connections.append(cave)
        cave.connections.append(self)

    def CanBeVisited(self):
        return self.visited == 0 and not self.isStartCave

    def Visit(self):
        if not self.isBigCave and not self.isStartCave:
            self.visited += 1

    def Unvisit(self):
        if not self.isBigCave:
            self.visited -= 1


run()
