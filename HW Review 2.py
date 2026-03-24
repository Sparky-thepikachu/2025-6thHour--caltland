#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW-R2

#1. Print "Hello World!"
print("Hello World!")
#2. Create an empty list.
empty_list = []
#3. Create a list that contains the names of everyone in the classroom.
robot_santas_list = ["Connor", "Devon", "Alaya", "Shane", "Ally", "Tristan",
                     "Ethan", "GREG"]

#4. Print the list from #3, sort the list, then print the list again.
print(robot_santas_list)
robot_santas_list.sort()
print(robot_santas_list)
#5. Append 5 different integers into the empty list from #2 and print the list.
empty_list.insert[1,2,3,4,5]
print(empty_list)
#6. Add together the middle three numbers in the list from #2 and print the result.
num_list = (empty_list[1] + empty_list[2] + empty_list[3])
print(num_list)
#7. Remove the very first number in the list from #2. Print the new first number.
num_list.remove(0)
print(num_list)

#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
valuedict = {
    "name": "Connor",
    "grade": 11,
    "favorte color": "yellow"
}
#9. Using the update function, add a fourth key and value determining your favorite candy.
valuedict.update({"favorite candy": "Reese"})
print(valuedict)
#10. Print ONLY the values of the dictionary from #8.
valuedict.pop("favorite candy")
print(valuedict)