#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW-R6

import random

#1. Create a def function that prints out "Hello World!". Call the function.
def hello_world():
    print("Hello World!")
hello_world()
#2. Create a def function that prints your name. Call the function with the name as the argument.
def class_name(name):
    print(name, "is in 6th Hour!")
class_name("Connor")
#3. Create a def function that calculates the average of a list. Call the function with the list as the argument.
def average(*num_list):
    average_num = sum(num_list) / len(num_list)
    print(average_num)
average(1,2,3,4,5,6,7)
#4. Call the function from #3 but with a new list of different numbers.
average(5,7,9,3,2)
#5. Create a def function that takes two numbers as arguments, x and y. Inside the function, create a for loop
#with a range of 10. Inside the loop, print x, make z equal the sum of x and y, make x equal y, then y equal z.
def fib(x,y):
    for i in range(10):
        print(x)
        z = x + y
        x = y
        y = z
#6. Call the function from #5 with the arguments for x and y being 0 and 1.
fib(0,1)