"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 2
-----------------------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Extend the functionality developed in Lab 1 by creating an InventoryManager class 
               that acts as a facade for managing an inventory of items. Demonstrate the use of 
               encapsulation and the facade design pattern through practical examples.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import the Item class from lab1.py
from lab1 import Item

# Step 2: Define the InventoryManager class as a facade to handle the inventory operations.
# It should include methods to add, remove, update, and display items in the inventory.

class InventoryManager():
    def __init__(self):
        self._items = []

    def add_item(self,item):
        self._items.append(item)

    def remove_item(self,item):
        self._items.remove(item)

    def display_items(self):
        print("All items:")
        for item in self._items:
            print(f"{item.get_name()}: Price - {item.get_price()} Qty - {item.get_qty}")

    


# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

def main():
    manager = InventoryManager
    item1 = Item("Sword", "500", "3")
    item2 = Item("Scythe", "1250", "0")
    item3 = Item("Dagger", "100", "8")

    manager.add_item(item1)
    manager.add_item(item2)
    manager.add_item(item3)
    manager.display_items()

if __name__ == "__main__":
    main()