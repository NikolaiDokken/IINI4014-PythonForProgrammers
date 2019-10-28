from graphics import *
import math


def main():

    # User inputs the window size, square length, and line width
    # Example: 500 500 50 10
    x, y, square, stroke = map(int, input(
        "Enter window size, sidelength(squares) and stroke width as: x y s w\n").split())
    # User inputs the colors of the grid, squares and circles
    # Example: black white red
    gridColor, squareColor, circleColor = map(str, input(
        "Enter colors as: grid squares circles\n").split())

    # Creates a window and sets background color (squares)
    win = GraphWin("Assignment 8", x, y)
    win.setBackground(squareColor)

    # Finds length of square + line, and checks how many lines we need in X and Y direction
    tempLen = square + stroke
    iterationsX = math.ceil(x / tempLen)
    iterationsY = math.ceil(y / tempLen)

    # Draw lines in X direction
    for i in range(iterationsY):
        line = Line(Point(0, tempLen*i), Point(x, tempLen*i))
        line.setWidth(stroke)
        line.setFill(gridColor)
        line.draw(win)

    # Draw lines in Y direction
    for i in range(iterationsX):
        line = Line(Point(tempLen*i, 0), Point(tempLen*i, y))
        line.setWidth(stroke)
        line.setFill(gridColor)
        line.draw(win)

    # Draw circles in every intersection
    for i in range(iterationsY):
        for k in range(iterationsX):
            circ = Circle(Point((k*tempLen), (i*tempLen)), stroke/2)
            circ.setFill(circleColor)
            circ.draw(win)

    win.getMouse()
    win.close()


main()
