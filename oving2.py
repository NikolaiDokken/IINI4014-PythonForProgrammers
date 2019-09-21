import math

# function for calculating pi with a given amount of iterations
# for each iteration, the amount of corners in the polygon doubles, starting at 6 
def archimedesPi(iterations):
	# starts by defining side length = 1
	s = 1
	# number of sides in the polygon in first iteration
	n = 6
	# defines the number of sides in each polygon given the iteration
	numberOfSides = math.pow(2,iterations-1)*n
	# loop that calculates the side length in each polygon
	for x in range(iterations - 1):
		a = math.sqrt(1-math.pow((s/2),2))
		b = 1-a
		s = math.sqrt(math.pow(b,2) + math.pow((s/2),2))			
	
	# archimedes method says pi = circumreferance / diameter which is 2
	pi = (s*numberOfSides)/2
	#prints out Pi as well as sides in the polygon
	print("Polygon with ", numberOfSides," sides, gives an estimate of Pi: ",pi)

# asks user how many iterations he/she wants
iterationsInput = int(input("How many iterations do you want?\n"))
# uses the function
archimedesPi(iterationsInput)


