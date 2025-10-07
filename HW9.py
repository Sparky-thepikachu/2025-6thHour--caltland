
#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW9

import random

#1. Print "Hello World!"
print ("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
random = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
#3. Print the list.
print(random)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if random[0] >= random[1] and random[0] >= random[2]:
    print(random[0])
elif random[1] >= random[0] and random[1] >= random[2]:
    print(random[1])
elif random[2] >= random[1] and random[2] >= random[0]:
    print(random[2])
#5. Tie the result (the largest number) from #4 to a variable called "num".
if random[0] >= random[1] and random[0] >= random[2]:
    num = (random[0])
elif random[1] >= random[0] and random[1] >= random[2]:
    num = (random[1])
elif random[2] >= random[1] and random[2] >= random[0]:
    num =(random[2])
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print("is divisible by 3 and 2")
