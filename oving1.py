# Allows user to enter their full name
fullName = input("Enter your full name: \n")

# Slits full name into separate names
names = fullName.split()

# Prints the first letter in every separate name = initials
print('Initials:', end = ' ')
for x in names:
    print(x[0], end = '')
print('\nWelcome to python for programmers ' + fullName + '! Hope you\'ll enjoy the course:)')