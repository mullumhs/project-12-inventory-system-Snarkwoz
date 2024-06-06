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

    def add_item(self,new_item):
        for item in self._items:
            if item.get_name() == new_item.get_name():
                print(f"{new_item.get_name()} is already in inventory")
                return
        self._items.append(new_item)
        print(f"{new_item.get_name()} added")

    def remove_item(self,del_item):
        for item in self._items:
            if item.get_name() == del_item:
                self._items.remove(del_item)
                print(f"Removed {del_item}")
                return

    def update_price(self,name,new_price):
        for item in self._items:
            if item.get_name() == name:
                item.set_price(new_price)
                return

    def display_items(self):
        print("All items:")
        for item in self._items:
            print(f"{item.get_name()}: Price - {item.get_price()} Qty - {item.get_qty()}")

# Step 2: Create instances of the Item class and InventoryManager, then demonstrate their usage.
# E.g. add items to the inventory, remove items, update items, and display the inventory.

def main():
    manager = InventoryManager()

    item1 = Item("Knife", "20", "4")
    item2 = Item("Totally not real gun", "200", "1")

    manager.add_item(item1)
    manager.add_item(item2)
    print("")
    manager.display_items()
    print("")
    manager.remove_item(item1)
    print("")
    manager.display_items()
    print("")
    manager.update_price(item2,"100")
    manager.display_items()

if __name__ == "__main__":
    main()