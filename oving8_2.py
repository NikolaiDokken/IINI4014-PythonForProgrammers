from tkinter import *
import math


def draw(bgColor, lineColor, dotColor, squareWidth, lineWidth, windowWidth, windowHeight, canvas):
    '''
    bgColor: string: color of the squares
    lineColor: string: color of grid lines
    dotColor: string: color of dots
    squareWidth: int: side-length of squares
    lineWidth: int: width of grid lines
    windowWidth: int: width of canvas
    windowHeight: int: height of canvas
    canvas: Canvas: canvas that is to be modified and drawn on
    '''
    canvas.delete(ALL)
    canvas.config(bg=bgColor, height=windowHeight, width=windowWidth)
    # Finds length of square + line, and checks how many lines we need in X and Y direction
    tempLen = squareWidth + lineWidth
    iterationsX = math.ceil(windowWidth / tempLen)
    iterationsY = math.ceil(windowHeight / tempLen)

    # Draw lines in X direction
    for i in range(iterationsY):
        canvas.create_line(0, tempLen*i, windowWidth,
                           tempLen*i, fill=lineColor, width=lineWidth)

    # Draw lines in Y direction
    for i in range(iterationsX):
        canvas.create_line(tempLen*i, 0, tempLen*i, windowHeight,
                           fill=lineColor, width=lineWidth)

    # Draw circles in every intersection
    for i in range(iterationsY):
        for k in range(iterationsX):
            canvas.create_oval((k*tempLen)-(lineWidth/2), (i*tempLen)-(lineWidth/2), (k*tempLen)+(lineWidth/2), (i*tempLen)+(lineWidth/2),
                               fill=dotColor, outline=dotColor)


def main():
    # Creates window
    window = Tk()
    window.title('Assignment 8')

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

    # Adds input for square size and line width, and sets default values
    Label(colorArea, text='Square size').grid(row=0, column=0)
    Label(colorArea, text='Grid line width').grid(row=1, column=0)

    squareSizeEntry = Entry(colorArea)
    lineWidthEntry = Entry(colorArea)
    squareSizeEntry.grid(row=0, column=1)
    lineWidthEntry.grid(row=1, column=1)

    squareSizeEntry.insert(0, 50)
    lineWidthEntry.insert(0, 10)

    # Adds input for colors in the color area, and sets default values
    Label(colorArea, text='Square color').grid(row=2, column=0)
    Label(colorArea, text='Line color').grid(row=3, column=0)
    Label(colorArea, text='Dot color').grid(row=4, column=0)

    squareColorEntry = Entry(colorArea)
    lineColorEntry = Entry(colorArea)
    dotColorEntry = Entry(colorArea)
    squareColorEntry.grid(row=2, column=1)
    lineColorEntry.grid(row=3, column=1)
    dotColorEntry.grid(row=4, column=1)

    squareColorEntry.insert(0, "black")
    lineColorEntry.insert(0, "white")
    dotColorEntry.insert(0, "black")

    def update():
        '''
        Method that updates the drawing on the canvas
        Runs when hitting the button
        '''
        draw(squareColorEntry.get(), lineColorEntry.get(),
             dotColorEntry.get(), int(squareSizeEntry.get()), int(lineWidthEntry.get()), int(widthEntry.get()), int(heightEntry.get()), canvas)

    # Button for updating canvas drawing
    drawButton = Button(colorArea, text="Draw", command=update)
    drawButton.grid(row=5)

    # Grid positioning of main areas
    canvasArea.grid(row=0, column=1)
    colorArea.grid(row=0, column=0)
    sizeArea.grid(row=1, column=0, columnspan=2)

    draw(squareColorEntry.get(), lineColorEntry.get(),
         dotColorEntry.get(), int(squareSizeEntry.get()), int(lineWidthEntry.get()), int(widthEntry.get()), int(heightEntry.get()), canvas)
    window.mainloop()


main()
