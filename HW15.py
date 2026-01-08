#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Insert integer number: "))
b = int(input("Insert integer number: "))
c = int(input("Insert integer number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
e = (a + b) / c
print(e)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(round(e))
#6. Create a list of five different random integers between 1 and 10.
random_list = [5,8,2,9,1]
#7. Print the 4th number in the list.
print("2")
#8. Append another integer to the end of the list, also random from 1 to 10.
random_list.append(6)
print(random_list)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
random_list.sort(reverse=True)
print(random_list)
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i < 100:
    if i ==100:
        break
    print(i)
    i +=1
#11. Create a list containing the names of five other students in the classroom.
name_list = ["Ethan","Kash","Eli","Tristin","Ally"]
#12. Create a for loop that individually prints out the names of each student in the list.
name_list.sort()
print(name_list)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
i = 1
while i < 100:
    if i ==100:
        break
    print(i)
    i +=1
#14. Free space. Do something creative. :)
word = ("Among us!")
repetition = 1000
for i in range(repetition):
    print(word)