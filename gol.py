class Cell:
    def __init__(self, x, y, i, j):
        self.isAlive = False
        self.nextStatus = None
        self.pos_screen = (x, y)
        self.pos_matrix = (i, j)

    def __str__(self):
        return str(self.isAlive)

    def __repr__(self):
        return str(self.isAlive)

    def switchStatus(self):
        self.isAlive = not self.isAlive
