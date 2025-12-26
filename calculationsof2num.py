
def multiply_numbers(x, y):
    return x * y
#end of function

#another function
def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
#end of function

#another function
def add_numbers(x, y):
    return x + y
#end of function

#another function
def subtract_numbers(x, y):
    return x - y
#end of function

#another function
def power_numbers(x, y):
    return x ** y
#end of function

#another function 
def modulus_numbers(x, y):
    return x % y
#end of function

#another function
def floor_divide_numbers(x, y):
    if y != 0:
        return x // y
    else:
        return "Error: Division by zero"
#end of function

#main code
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operation = input("Enter operation (multiply, divide, add, subtract, power, modulus, floor_divide): ")

if operation == "multiply":
    print("Result:", multiply_numbers(x, y))
elif operation == "divide":
    print("Result:", divide_numbers(x, y))
elif operation == "add":
    print("Result:", add_numbers(x, y))
elif operation == "subtract":
    print("Result:", subtract_numbers(x, y))
elif operation == "power":
    print("Result:", power_numbers(x, y))
elif operation == "modulus":
    print("Result:", modulus_numbers(x, y))
elif operation == "floor_divide":
    print("Result:", floor_divide_numbers(x, y))
else:
    print("Invalid operation")
