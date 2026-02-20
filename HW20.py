#Name: Connor Altland
#Class: 6th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class store_items:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double_cost(self):
        self.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
Pichu = store_items(100, 10, 2)
Pikachu = store_items(50, 50, 13.2)
Raichu = store_items(10, 100, 66.1)
#3. Print the stock of all three objects and the cost of the second store item.
print("Pichu stock: ", Pichu.stock)
print("Pikachu stock: ", Pikachu.stock)
print("Raichu stock: ", Raichu.stock)

print("Pikachu cost:",Pikachu.cost)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
Pikachu.double_cost()
print("Pikachu cost:",Pikachu.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
Raichu.stock /= 4
Raichu.stock = (round(Raichu.stock))
print("Raichu stock: ", Raichu.stock)
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.

del Pichu

try:
    print(pichu.weight)
except:
     print("Pichu is out of stock")
