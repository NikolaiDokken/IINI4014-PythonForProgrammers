import time

def isPrime(numb):
	# Numbers equal to 1 or lower are not prime numbers
	if (numb <= 1):
		return False
	# 2 and 3 are prime numbers, and kind of unique
	if (numb <= 3):
		return True
	# if numb is divisible by two or three it is not a prime number
	if (numb % 2 == 0 or numb % 3 == 0):
		return False
	
	# if numb passes the tests above, but is lower than 25 it will automatically be a prime number and return true. if numb is greater than or equal to 25, it will run the loop and check every number from 5 to the square root of numb 
	i = 5
	while(i*i <= numb):
		if (numb % i == 0):
			return False
		i = i+1
	return True
	
amt = 1000
list = []
testNumb = 0

# added timer for test purposes
startTime = time.time()
# loop that runs until the first 1000 prime numbers are found
while(len(list) < amt):
	if (isPrime(testNumb)):		
		list.append(testNumb)
	testNumb = testNumb+1
endTime = time.time()
print((endTime-startTime)*1000)
