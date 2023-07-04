import csv 
class Item:
    # attribute on the class level -> will exist for all intsances of this class 
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # create a list to store all instances of this Class

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero"
        assert quantity >= 0,f"Quantity {quantity} is not greater or equal than zero"
        
        # Assign to self object
        self.__name = name           # __ prevents the access to __name from outside the class 
        self.__price = price
        self.quantity = quantity

        # Actions to execute 
        Item.all.append(self)   # append instance to all list
    
    # Encapsuplte principle: don't allow direct access to attribute but only through methods below 
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate   # access the attribute "pay_rate" from the item level

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decorator = Read-ONly Attribute 
    # the class now has a read only attribute "name" which we can access from outside the class 
    # -> returns the not accessibly __name 
    def name(self):          
        return self.__name
    
    # Adds a setter to the name attribute 
    @name.setter
    def name(self, value):
        print("You are trying to set")
        if len(value) > 10: 
            raise Exception("The name is too long!")
        else:
            self.__name = value 

    def calculate_total_price(self):
        return self.__price * self.quantity

    
    
    
    # in a class method the class must be passed as first object 
    @classmethod
    def instatiate_from_csv(cls):
        with open('items.csv', 'r') as f: 
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'), 
                price=float(item.get('price')), 
                quantity=int(item.get('quantity')),
            )
    
    # static methods never passes the object itself as the first argument 
    # refer to it as a regular function 
    @staticmethod
    def is_this_a_integer(num):
        if isinstance(num, float): 
            return num.is_integer()
        elif isinstance(num, int): 
            return True 
        else: 
            return False 
    
    # edit the representation of the Object
    # Best practice to represent exectly how you call the object to create an instance  
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"