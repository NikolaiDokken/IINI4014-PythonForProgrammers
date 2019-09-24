import turtle
import math

# Method that uses generator and yield keyword to find positions
# Points are found based on multiplier and amout of points
def findPositions(multiplier, points):
    nums = [0]
    for x in range(points):
        if (x != 0):
            nums.append(x)
    for i in nums:
        yield((i*multiplier) % points)

# Method makes turtle draw with a given muliplier and amount of points
def draw(bot, multiplier, points):
    #defines a radius and degrees between points
    radius = 280
    currentPos = 0;
    degrees = 360 / points
    destinationPoints = findPositions(multiplier, points)
 
    # Moves the turtle to starting point 0, on the left side of the window
    bot.penup()
    bot.goto(-radius,0)
    xPrev = 0
    yPrev = 0
    xPos = 0
    yPos = 0
    bot.pendown()
    
    # Loop that draws the actual figure
    # X=cos(x)  Y=sin(x)
    while currentPos < points:

        # Gets next position from the generator
        # Could also have been calculated directly here
        nextPos = next(destinationPoints)
        # finds x and y coordinates for given point
        xPos = math.cos(math.radians(180-(degrees*(nextPos))))*radius
        yPos = math.sin(math.radians(180-(degrees*(nextPos))))*radius 
        # draws a line to the new point, then goes back
        xPrev = xPos
        yPrev = yPos
        bot.goto(xPos, yPos)
        bot.goto(xPrev, yPrev)
        
        # moves the turtle to the next point
        bot.penup()
        xPos = math.cos(math.radians(180-(degrees*(currentPos+1))))*radius
        yPos = math.sin(math.radians(180-(degrees*(currentPos+1))))*radius
        bot.goto(xPos, yPos)
        bot.pendown()
        currentPos += 1
        
def main():
    multiplier = int(input("What multiplier do you want?\n"))
    points = int(input("How many points do you want?\n"))
    bot = turtle.Turtle()
    bot.speed(0)
    myWin = turtle.Screen()
    draw(bot, multiplier, points)
    myWin.exitonclick()

main()
