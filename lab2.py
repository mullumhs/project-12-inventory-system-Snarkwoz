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

    def add_item(self,name,price,qty):
        for item in self._items:
            if item.name == name:
                print(f"{name} is already in inventory")
                return
        self._items.append(name,price,qty)

    def remove_item(self,name):
        for item in self._items:
            if item.name == name:
                self._items.remove(name)
                print(f"Removed {name}")
                return
    
    def update_item(self,name,new_price=None,new_qty=None):
        for item in self._items:
            if item.get_name() == name:
                item.set_price(new_price)
                item.set_qty(new_qty)

    def display_items(self):
        print("All items:")
        for item in self._items:
            print(f"{item.get_name()}: Price - {item.get_price()} Qty - {item.get_qty}")

# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

def main():
    manager = InventoryManager

    item1 = Item("Knife", "20", "4")
    item2 = Item("Glock", "200", "1")

    manager.add_item(item1)
    manager.add_item(item2)

    manager.display_items()

if __name__ == "__main__":
    main()