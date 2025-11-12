#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW14

import random
import time

x = random.randint(6,10)
print(x)
#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
i = 5
for i in range(5,0,-1):
    print(i)
else:
    print("Hello World")

#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
j = 3
for j in range(2,31,2):
    print(j)
    for j in range(1,31):
        if j % 2 == 0:
                print(j)

#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for k in range(1,31):
    if k % 3 == 0:
        continue
    print(k)
#4. Create a for loop that prints 5 different animals from a list.
animals = ["monkey","cat","dog","rabbit","tiger" ]
for animal in animals:
    print(animal)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for w in input("give me a word: ")[::-1]:
    print(w)

#6. Create a list containing 10 integers of your choice and print the list.
my_integer =[10,20,30,40,50,60,70,80,90,100]
print(my_integer)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = []
oddNumbers = []
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
#9. Create a variable that asks the user for an integer and an empty integer variable.
# Variable to store the integer input from the user
user_integer = None  # Initialize as None to represent an empty state

# Loop to repeatedly ask for input until a valid integer is provided
while user_integer is None:
    try:
        # Prompt the user for an integer and convert the input string to an integer
        user_integer = int(input("Please enter an integer: "))
    except ValueError:
        # Handle cases where the input is not a valid integer
        print("Invalid input. Please enter a whole number.")

# An empty integer variable (initialized to a value that indicates "empty" or "not set")
empty_integer_variable = 0 # Or you could use None, depending on your needs.
                           # Using 0 is common if 0 is a valid default or starting point.
                           # Using None is common when a value is truly absent.

print(f"The integer you entered is: {user_integer}")
print(f"The empty integer variable is: {empty_integer_variable}")
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)

# Get the number from the user
try:
    num = int(input("Enter a non-negative integer to calculate its factorial: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
else:
    # Check for negative numbers
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    # Handle the case of 0!
    elif num == 0:
        print("The factorial of 0 is 1.")
    else:
        factorial = 1
        # Calculate the factorial using a loop
        for i in range(1, num + 1):
            factorial *= i
        print(f"The factorial of {num} is {factorial}.")