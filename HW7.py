#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW7


#1. Print Hello World!
print('Hello world')
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
FavoriteCarDict = {
"brand" : "Ford",
"Model" : "RS200",
"Year" : [1984,1985,1986]
}
#3. Print the keys of the dictionary from #2.
print(FavoriteCarDict.keys())
#4. Print the values of the dictionary from #2
print(FavoriteCarDict.values())
#5. Print one of the three numbers from the list by itself
print(FavoriteCarDict["Year"][0])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
FavoriteCarDict.update({"Terrain" : "Rally"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(FavoriteCarDict)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
Sixth_hour_Class = {
    "student_1": {
        "Name": "Ethan",
        "Grade": 9,
        "Sports":True,
    },
    "student_2": {
        "Name": "Tristin",
        "Grade": 9,
        "Sports": True,
    },
    "student_3": {
        "Name": "Kash",
        "Grade": 12,
        "Sports": True,
    },
}
#9. Print the names of all three classmates on the same line.
print(Sixth_hour_Class["student_1"]["Name"],Sixth_hour_Class["student_2"]["Name"],Sixth_hour_Class["student_3"]["Name"],)
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
Sixth_hour_Class.pop("student_3")
print(Sixth_hour_Class)