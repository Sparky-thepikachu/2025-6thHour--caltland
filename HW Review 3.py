#Name: Connor Altland
#Class: 5th Hour
#Assignment: HW-R3

import random
#1. import random and print "Hello World!"
print("Hello World")
#2. Create three variables that each randomly generate an integer between 1 and 10, print each number on the same line.
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
print(a, b, c)
#3. Create a list containing 5 strings listing 5 colors.
color_list = ['red', 'blue', 'green', 'yellow', "sky blue"]
print(random.choice(color_list))
#4. Use a function to randomly choose one of the 5 colors from the list and print the result.
def random_color():
    r = random.randint(0,5)
#5. Create an if statement that determines which of the three variables from #2 is the lowest.
if a < b and a < c:
    print(a)
elif b < c and b < a:
    print(b)
else :
    print(c)