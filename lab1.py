"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 1
-----------------------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class named Item that represents a generic item in an inventory system.
               Implement encapsulation using private attributes and public getters and setters.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Define the Item class with initialisation that uses setters for name, price, and quantity.
# Instead of directly setting private attributes in the __init__ method, use the class's own setters
# We will define the setters in later steps to add validation to the setting of these attributes.

class Item():
    def __init__(self,name,price,qty):
        self._name = name
        self._price = price
        self._qty = qty

    # getters
    def get_name(self):
        print(self._name)

    def get_price(self):
        print(f"${int(self._price):.2f}")

    def get_qty(self):
        print(f"You have {self._qty} {self._name}s")

    #setters
    def set_price(self,new_price):
        if not new_price.isdigit() or int(new_price) < 0:
            raise ValueError("Price cannot be negative") 
        self._price = new_price

    def set_qty(self,new_qty):
        if not new_qty.isdigit() or int(new_qty) < 0:
            raise ValueError("Has to be a number greater than zero")
        self._qty = new_qty


sword = Item("Sword","2000","1")
kaboom = Item("Bomb","25","12")

sword.set_price("2500")
sword.set_qty("2")
sword.get_name()
sword.get_price()
sword.get_qty()
print("")
kaboom.set_price("20")
kaboom.set_qty("15")
kaboom.get_name()
kaboom.get_price()
kaboom.get_qty()

# Step 2: Implement a getter for the name attribute.
# This method should simply return the value of the private _name attribute.

# Step 3: Implement a setter for the name attribute.
# This method should check if the provided value is a string before setting the _name attribute.
# If the value is not a string, it should raise a ValueError.

# Step 4: Implement a getter for the price attribute.
# This method should return the price formatted as a string with two decimal places.

# Step 5: Implement a setter for the price attribute.
# This method should check if the provided value is a non-negative number before setting the _price attribute.
# If the value is negative, it should raise a ValueError.

# Step 6: Implement a getter for the quantity attribute.
# This method should simply return the value of the private _quantity attribute.

# Step 7: Implement a setter for the quantity attribute.
# This method should check if the provided value is a non-negative integer before setting the _quantity attribute.
# If the value is negative, it should raise a ValueError.

# Step 8: Create instances of the Item class and demonstrate the use of getters and setters.
# For example, create a new Item and attempt to set its attributes with both valid and invalid values.
# Print the outputs using the getters to show how the data is managed internally.
