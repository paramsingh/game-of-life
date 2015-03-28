class Cell:
    def __init__(self, x, y):
        self.isAlive = False
        self.pos = (x, y)

    def __str__(self):
        return str(self.isAlive)

    def __repr__(self):
        return str(self.isAlive)

    def changeStatus(self):
        self.isAlive = not self.isAlive

    def findNextStatus(self):
        pass


class Board:
    def __init__(self, x):
        self.values = []
        self.limit = x
        for i in range(self.limit):
            self.values.append([])
            for j in range(self.limit):
                self.values[i].append(Cell(i, j))
