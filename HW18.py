#Name:Connor Altland
#Class: 6th Hour
#Assignment: HW18

import random

#1. Import the "random" library and create a def function that prints "Hello World!"
def hello_world():
    print("Hello World!")
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def flip_coin_100_times():
    global heads, tails

    for i in range(100):
        flip = random.choice(["heads", "tails"])
        if flip == "heads":
            heads += 1
        else:
            tails += 1
#4. Call the "Hello world" and "Coin Flip" functions here
hello_world()
flip_coin_100_times()
#5. Print the final result of heads and tails here
print("heads:", tails)
print("tails:", tails)
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag_list = ["yellow bean","red bean","black bean","blue bean","white bean"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def pull_bean(beanBag):
    if len(beanBag) == 0:
        print("No beans")
bean = random.choice(beanBag_list)
print("you pulled:", bean)
beanBag_list.remove(bean)
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def pull_again(beanBag):
    while True:
        answer = input("Do you want to pull again? (y/n): ").lower()
        if answer == "y":
            pull_bean(beanBag)
            print("no more beans in the bag")
            break
        elif answer == "n":
            print("done pulling beans")
            break
        else:
            print("please y or n")
#9. Call the "Bean Pull" function here
pull_bean(beanBag_list)
pull_again(beanBag_list)