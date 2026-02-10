#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW19

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import animal_list, hello_world, average, number_list
#2. Call the functions here and run HW19
animal_list("kitty","bunny", "puppy", "cub","calf")
hello_world()
average(7,3,1)
number_list(5)
#3. Delete all calls for problem 5 in HW16 and run HW19 again.

#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except:
    print("Hello World!")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num_div = int(input("Give me an integer: "))
    print(100/num_div)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Value Error. Needs to be an integer!")
except:
    print("Unknown error.")
#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    print(y)
except:
    print("Something went wrong!")
finally:
    print("This is the end of the Try Except!")

#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
num_count = 5

while num_count >= 0:
    print(num_count)
    if num_count == 0:
        print("count reached zero. Now checking for next value.")
    num_count -= 1
    if num_count < 0:
        raise ValueError("Count cannot be less than zero.")

print("This line will not be executed because an exception was raised.")