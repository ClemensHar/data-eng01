from item import Item 
from phone import Phone

item1 = Item("MyItem", 750, 6)
print(item1.name)



###
# Applying properties of the class and rea
item1.name = "newName" 
print(item1.name)

print(item1.price)

item1.apply_increment(0.2)
print(item1.price)

