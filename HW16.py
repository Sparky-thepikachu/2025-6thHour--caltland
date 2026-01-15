#Name:Connor Altland
#Class: 6th Hour
#Assignment: HW16

import random

#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")


#2. Create a def function that calculates the average of three numbers (set the 3 numbers as your arguments).
def average(num1, num2, num3):
    avg = (num1 + num2 + num3) / 3
    print(avg)
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*animals):
    print("The 5th animal is:", animals[2])

#4. Create a def function that loops from 1 to the number put in the argument.
def number_list(count):
    for i in range(1, count + 1):
        print(i)


#5. Call all of the functions created in 1 - 4 with relevant arguments.
animal_list("kitty","bunny", "puppy", "cub","calf")
average(7,3,1)
hello_world()
number_list(5)
#6. Create a variable x that has the value of 2. Print x
x = 2
print(x)
#7. Create a def function that multiplies the value of 2 by a random number between 1 and 5.
def make_x_2():
    global x
    x = x * random.randint(1, 5)

def print_new_x():
    print(x)
#8. Print the new value of x.
make_x_2()
print_new_x()