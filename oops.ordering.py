
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def show_details(self):
        print("Order is of",self.item,"whose price is",self.price)

    def __gt__(self,another):
        return self.price > another.price
    
class Preference(Order):
    def __gt__(self, another):
        return super().__gt__(another)
    
fruits = {
    "apple":150,
    "banana":100,
    "Orange":150,
    "pineapple":200
} 
order1 = input("Enter fruit you wanna purchase=")
price =  fruits.get(order1.lower(),0)
if price == 0:
    print("Fruit is not available!!")
else:

    item1 = Order(order1, fruits.get(order1.lower(), 0))
    item1.show_details()

order2 = input("Enter fruit you wanna purchase=")
price = fruits.get(order2.lower(), 0)
if price == 0:
    print("Fruit is not available!!")
else:
    item2 = Order(order2, fruits.get(order2.lower(), 0))
    item2.show_details()

comp = input("Do you want to compare(y/n)=")
if comp == "y":
    if item1 > item2:
        print("Order placed first has higher price!!")
    elif item1.price ==0:
        print("Sorry we can't compare!!")
    elif item2.price == 0:
        print("Sorry we can't compare!!")
    else:
        print("2nd Order placed has higher price!!")
else:
    print("As your wish,Sir!!")
