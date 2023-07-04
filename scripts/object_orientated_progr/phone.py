import csv 
from item import Item

# create new child class inheritating from the Item class 
class Phone(Item):
    pay_rate = 0.4      # we can overwrite this value from the parent class 
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes/methods
        # Basically calls the __init__ function in the parent Class  
        super().__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        # Assign to self object - This is a method belonging only to the child class not the parent class 
        self.broken_phones = broken_phones

         


phone1 = Phone("jscPhonev10", 500, 5,1)
phone2 = Phone("jscPhonev20", 700, 5,1)

# print(phone1.calculate_total_price())
# print(phone2.name)

print(Item.all)
print(Phone.all)