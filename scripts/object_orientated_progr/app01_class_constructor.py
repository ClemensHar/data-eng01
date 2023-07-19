from item import Item


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


item2.has_numpad = False

# apply discount
print("Old price")
print(item1.__price)
print("Price after applying discount")
item1.apply_discount()
print(f"Discounted price of item {item1.name}")
print(item1.__price)

print(f"Discounted price of item {item2.name}")
item2.pay_rate = 0.1  # this will change the attribute on the instance level but not on the Class level
item2.apply_discount()
print(item2.__price)

# print the list covering all instances of the Class
print(Item.all)

# iterate through all instance of the Class and print out name
for instance in Item.all:
    print(instance.name)
