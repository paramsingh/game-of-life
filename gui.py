from Tkinter import *
from gol import *

root = Tk()
frame = Frame(root, width=520, height=520)
frame.pack()
canvas = Canvas(frame, width=520, height=520)
canvas.pack()

def create_grid():
    """This function creates the board on which the game will take place"""
    x = 10
    y = 10
    global grid # Variable to store the Cell objects
    grid = []
    for i in range(50):
        grid.append([])
        for j in range(50):
            canvas.create_rectangle(x, y, x+10, y+10)
            grid[i].append(Cell(x, y))
            x += 10
        x = 10
        y += 10

def find_rect_coordinates(x, y):
    """Find the co-ordinates of the rectangle which has been clicked"""
    return (x- x%10, y - y%10)

def change_colour_on_click(event):
    """ Change the colour of the clicked grid and change the status of cell in the grid """
    print event.x, event.y
    x, y = find_rect_coordinates(event.x, event.y)
    try:
        ix = x / 10
        iy = y / 10
        if ix == 0 or iy == 0:
            raise IndexError
        grid[ix][iy].changeStatus()
    except IndexError:
        return
    canvas.create_rectangle(x, y, x+10, y+10, fill="green")
    print grid[x/10][y/10]


def paint_grid():
    for x, i in enumerate(grid):
        for y, j in enumerate(i):
            if j.isAlive:
                canvas.create_rectangle(x, y, x+10, y+10, fill="green")


def diffStatus(cell):
    pass


def begin_game():
    while True:
        for i in grid:
            for j in i:
                if diffStatus(j):
                    self.nextStatus = not self.isAlive
                else:
                    self.nextStatus = self.isAlive
        paint_grid()


create_grid()
start = Button(root, text="Start!", command=begin_game)
start.pack()
canvas.bind("<Button-1>", change_colour_on_click)
root.mainloop()
