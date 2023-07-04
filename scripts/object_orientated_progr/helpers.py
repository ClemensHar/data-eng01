class Item:
    # attribute on the class level -> will exist for all intsances of this class 
    pay_rate = 0.8 # The pay rate after 20% discount
    all = [] # create a list to store all instances of this Class

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater or equal than zero"
        assert quantity >= 0,f"Quantity {quantity} is not greater or equal than zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute 
        Item.all.append(self)   # append instance to all list 
        

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate   # access the attribute "pay_rate" from the item level

    def instatiate_from_csv(self):
        pass
    
    # edit the representation of the Object
    # Best practice to represent exectly how you call the object to create an instance  
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"