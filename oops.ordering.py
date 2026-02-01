class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def show_details(self):
        print("Order is of", self.item, "whose price is", self.price)

    def __gt__(self, another):
        return self.price > another.price
    

class Preference(Order):
    def __gt__(self, another):
        return super().__gt__(another)


# Fruit dictionary (all lowercase for consistency)
fruits = {
    "apple": 150,
    "banana": 100,
    "orange": 150,
    "pineapple": 200
}

# Show all fruits
print("Available fruits:")
for i in fruits:
    print(i)

# Initialize orders
item1 = None
item2 = None

# Taking first order
order1 = input("Enter fruit you wanna purchase=")
price = fruits.get(order1.lower(), 0)
if price == 0:
    print("Fruit is not available!!")
else:
    item1 = Order(order1, price)
    item1.show_details()

# Taking second order
order2 = input("Enter fruit you wanna purchase=")
price = fruits.get(order2.lower(), 0)
if price == 0:
    print("Fruit is not available!!")
else:
    item2 = Order(order2, price)
    item2.show_details()

# Handling total calculation
total = 0
if item1:
    total += item1.price
if item2:
    total += item2.price

print("Your total order is of", total)

# Asking for comparison
comp = input("Do you want to compare(y/n)=")
if comp.lower() == "y":
    if item1 and item2:
        if item1 > item2:
            print("Order placed first has higher price!!")
        elif item1.price == item2.price:
            print("Both orders have the same price!!")
        else:
            print("2nd Order placed has higher price!!")
    else:
        print("Sorry we can't compare!!")
else:
    print("As your wish, Sir!!")
