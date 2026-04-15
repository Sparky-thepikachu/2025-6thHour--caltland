#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW_R8


#1. Import all of HW_R7 into this assignment using the from/import function.
from HW_R7 import *
#2. Create an object of three students in the classroom. Ask for their name, grade, and favorite color as need be.
Ethan = student("Ethan", 9, "red")
Tristan = student("Tristan", 9, "purple")
Greg = student("Greg", 12, "purple")
#3. Print the name of the first student.
print("Ethan")
#4. Use the def function from HW_R7 to bump the grade level of the second student up by 1. Print the new grade.
Tristan.add_grade()
print("Tristan new grade is:", Tristan.grade)
#5. Use the def function from HW_R7 to ask the third student to change their favorite color to something else.
#Print the new color.
Greg.change_color()
print("Greg's new favorite color is:", Greg.color )

