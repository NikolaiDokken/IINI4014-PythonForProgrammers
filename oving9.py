import random
from tkinter import *


class Dice:
    def __init__(self, window, xPos, yPos, size, bgColor='black', dotColor='white'):
        """
        Constructor for Dice
        window: GraphWin: the canvas that will be drawn on
        xPos: int: dice's upper left corner x coordinate
        yPos: int: dice's upper left corner y coordinate
        size: int: dices's side-length
        bgColor: string: color of the dice, optional, defaults to black
        dotColor: string: color of dice's dots, optional, defaults to white

        """
        self.xPos = xPos
        self.yPos = yPos
        self.bgColor = bgColor
        self.dotColor = dotColor
        self.window = window
        self.size = size

    def getXPos(self):
        """
        Gets dice's upper left corner's x coorinate
        return: int: x coordinate
        """
        return self.xPos

    def getYPos(self):
        """
        Gets dice's upper left corner's y coorinate
        return: int: y coordinate
        """
        return self.yPos

    def getSize(self):
        """
        Gets dice's side-length
        return: int: side-length
        """
        return self.size

    def rollDice(self):
        """
        Rolls the dice
        return: int: random number from 1 to 6
        """
        return random.randrange(1, 7)

    def drawDice(self):
        """
        Draws the dice with random amount of dots
        """
        self.window.delete(ALL)
        eyes = self.rollDice()
        diceSideLength = self.size

        self.window.create_rectangle(self.xPos, self.yPos,
                                     self.xPos+diceSideLength, self.yPos+diceSideLength, fill=self.bgColor)

        # Different patterns for different dice sides
        if (eyes == 1):
            self.window.create_oval(self.xPos+diceSideLength/2-diceSideLength/10, self.yPos+diceSideLength/2-diceSideLength/10,
                                    self.xPos+diceSideLength/2+diceSideLength/10, self.yPos+diceSideLength/2+diceSideLength/10, fill=self.dotColor)
        elif (eyes == 2):
            self.window.create_oval(self.xPos+diceSideLength/3-diceSideLength/10, self.yPos+diceSideLength/3-diceSideLength/10,
                                    self.xPos+diceSideLength/3+diceSideLength/10, self.yPos+diceSideLength/3+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+2*diceSideLength/3-diceSideLength/10, self.yPos+2*diceSideLength/3-diceSideLength/10,
                                    self.xPos+2*diceSideLength/3+diceSideLength/10, self.yPos+2*diceSideLength/3+diceSideLength/10, fill=self.dotColor)

        elif (eyes == 3):
            self.window.create_oval(self.xPos+2*diceSideLength/8-diceSideLength/10, self.yPos+2*diceSideLength/8-diceSideLength/10,
                                    self.xPos+2*diceSideLength/8+diceSideLength/10, self.yPos+2*diceSideLength/8+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+4*diceSideLength/8-diceSideLength/10, self.yPos+4*diceSideLength/8-diceSideLength/10,
                                    self.xPos+4*diceSideLength/8+diceSideLength/10, self.yPos+4*diceSideLength/8+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+6*diceSideLength/8-diceSideLength/10, self.yPos+6*diceSideLength/8-diceSideLength/10,
                                    self.xPos+6*diceSideLength/8+diceSideLength/10, self.yPos+6*diceSideLength/8+diceSideLength/10, fill=self.dotColor)

        elif (eyes == 4):

            self.window.create_oval(self.xPos+diceSideLength/4-diceSideLength/10, self.yPos+diceSideLength/4-diceSideLength/10,
                                    self.xPos+diceSideLength/4+diceSideLength/10, self.yPos+diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+3*diceSideLength/4-diceSideLength/10, self.yPos+diceSideLength/4-diceSideLength/10,
                                    self.xPos+3*diceSideLength/4+diceSideLength/10, self.yPos+diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+diceSideLength/4-diceSideLength/10, self.yPos+3*diceSideLength/4-diceSideLength/10,
                                    self.xPos+diceSideLength/4+diceSideLength/10, self.yPos+3*diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+3*diceSideLength/4-diceSideLength/10, self.yPos+3*diceSideLength/4-diceSideLength/10,
                                    self.xPos+3*diceSideLength/4+diceSideLength/10, self.yPos+3*diceSideLength/4+diceSideLength/10, fill=self.dotColor)

        elif (eyes == 5):
            self.window.create_oval(self.xPos+diceSideLength/4-diceSideLength/10, self.yPos+diceSideLength/4-diceSideLength/10,
                                    self.xPos+diceSideLength/4+diceSideLength/10, self.yPos+diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+3*diceSideLength/4-diceSideLength/10, self.yPos+diceSideLength/4-diceSideLength/10,
                                    self.xPos+3*diceSideLength/4+diceSideLength/10, self.yPos+diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+diceSideLength/4-diceSideLength/10, self.yPos+3*diceSideLength/4-diceSideLength/10,
                                    self.xPos+diceSideLength/4+diceSideLength/10, self.yPos+3*diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+3*diceSideLength/4-diceSideLength/10, self.yPos+3*diceSideLength/4-diceSideLength/10,
                                    self.xPos+3*diceSideLength/4+diceSideLength/10, self.yPos+3*diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+diceSideLength/2-diceSideLength/10, self.yPos+diceSideLength/2-diceSideLength/10,
                                    self.xPos+diceSideLength/2+diceSideLength/10, self.yPos+diceSideLength/2+diceSideLength/10, fill=self.dotColor)

        else:
            self.window.create_oval(self.xPos+diceSideLength/4-diceSideLength/10, self.yPos+diceSideLength/4-diceSideLength/10,
                                    self.xPos+diceSideLength/4+diceSideLength/10, self.yPos+diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+2*diceSideLength/4-diceSideLength/10, self.yPos+diceSideLength/4-diceSideLength/10,
                                    self.xPos+2*diceSideLength/4+diceSideLength/10, self.yPos+diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+3*diceSideLength/4-diceSideLength/10, self.yPos+diceSideLength/4-diceSideLength/10,
                                    self.xPos+3*diceSideLength/4+diceSideLength/10, self.yPos+diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+diceSideLength/4-diceSideLength/10, self.yPos+3*diceSideLength/4-diceSideLength/10,
                                    self.xPos+diceSideLength/4+diceSideLength/10, self.yPos+3*diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+2*diceSideLength/4-diceSideLength/10, self.yPos+3*diceSideLength/4-diceSideLength/10,
                                    self.xPos+2*diceSideLength/4+diceSideLength/10, self.yPos+3*diceSideLength/4+diceSideLength/10, fill=self.dotColor)

            self.window.create_oval(self.xPos+3*diceSideLength/4-diceSideLength/10, self.yPos+3*diceSideLength/4-diceSideLength/10,
                                    self.xPos+3*diceSideLength/4+diceSideLength/10, self.yPos+3*diceSideLength/4+diceSideLength/10, fill=self.dotColor)


def main():
    # Creates window
    window = Tk()
    window.title('Assignment 9')

    # Creates different areas
    canvasArea = Frame(window)
    colorArea = Frame(window)
    sizeArea = Frame(window)

    # Makes a canvas in the canvas area
    canvas = Canvas(canvasArea)
    canvas.pack()

    # Adds input for canvas size in the size area, and sets default values
    Label(sizeArea, text='Height').grid(row=1, column=0)
    Label(sizeArea, text='Width').grid(row=2, column=0)
    heightEntry = Entry(sizeArea)
    widthEntry = Entry(sizeArea)
    heightEntry.grid(row=1, column=1)
    widthEntry.grid(row=2, column=1)

    heightEntry.insert(0, 500)
    widthEntry.insert(0, 500)

    # Adds input for dice size, and sets default values
    Label(colorArea, text='Dice size').grid(row=0, column=0)

    squareSizeEntry = Entry(colorArea)
    squareSizeEntry.grid(row=0, column=1)

    squareSizeEntry.insert(0, 100)

    # Adds input for colors in the color area, and sets default values
    Label(colorArea, text='Dice color').grid(row=2, column=0)
    Label(colorArea, text='Dot color').grid(row=3, column=0)

    squareColorEntry = Entry(colorArea)
    dotColorEntry = Entry(colorArea)
    squareColorEntry.grid(row=2, column=1)
    dotColorEntry.grid(row=3, column=1)

    squareColorEntry.insert(0, "white")
    dotColorEntry.insert(0, "black")

    # Adds input for x and y position of dice, and sets default values
    Label(colorArea, text='X position').grid(row=4, column=0)
    Label(colorArea, text='Y position').grid(row=5, column=0)

    xPos = Entry(colorArea)
    yPos = Entry(colorArea)
    xPos.grid(row=4, column=1)
    yPos.grid(row=5, column=1)

    xPos.insert(0, 200)
    yPos.insert(0, 200)

    def update():
        '''
        Method that updates the drawing on the canvas
        Runs when hitting the button
        '''
        canvas.config(width=int(widthEntry.get()),
                      height=int(heightEntry.get()))
        Dice(canvas, int(xPos.get()), int(yPos.get()), int(
            squareSizeEntry.get()), squareColorEntry.get(), dotColorEntry.get()).drawDice()

    # Button for updating canvas drawing
    drawButton = Button(colorArea, text="Roll and Draw", command=update)
    drawButton.grid(row=6)

    # Grid positioning of main areas
    canvasArea.grid(row=0, column=1)
    colorArea.grid(row=0, column=0)
    sizeArea.grid(row=1, column=0, columnspan=2)

    # Configurates canvas, and draws the default dice with random amount of dots
    canvas.config(width=widthEntry.get(), height=heightEntry.get())
    test = Dice(canvas, int(xPos.get()), int(yPos.get()), int(
        squareSizeEntry.get()), squareColorEntry.get(), dotColorEntry.get())
    test.drawDice()
    window.mainloop()


main()
