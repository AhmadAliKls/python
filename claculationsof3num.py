
def greater_number(a, b, c):
    if a>b and a>c:
        return(a)
    elif b>a and b>c:
        return(b)
    elif a==b and a>c:
        return(a , b )
    elif a==c and a>b:
        return(a, c)
    elif b==c and b>a:
        return(b, c)
    elif a==b and a==c:
        return(a, b, c)
    else:
        return(c)
#end of function

#another function 

def average_number(a, b, c):
    avg = (a + b + c) / 3
    return avg  
#end of function

#another function
def sum_number(a, b, c):
    sum = a + b + c
    return sum
#end of function

#another function 

def product_number(a, b, c):
    product = a * b * c
    return product 
#end of function

#another function 
def smallest_number(a, b, c):
    if a<b and a<c:
        return(a)
    elif b<a and b<c:
        return(b)
    elif a==b and a<c:
        return(a , b )
    elif a==c and a<b:
        return(a, c)
    elif b==c and b<a:
        return(b, c)
    elif a==b and a==c:
        return(a, b, c)
    else:
        return(c)
#end of function

#main code
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
num = input("Enter the function you want to perform (greater, smallest, average, sum, product): ")


if num == "greater":
    result = greater_number(a, b, c)
    print(result, "is the greatest number")
elif num == "smallest":
    result = smallest_number(a, b, c)
    print(result, "is the smallest number")
elif num == "average":
    result = average_number(a, b, c)
    print(result, "is the average of the numbers")
elif num == "sum":
    result = sum_number(a, b, c)
    print(result, "is the sum of the numbers")
elif num == "product":
    result = product_number(a, b, c)
    print(result, "is the product of the numbers")
else:
    print("Invalid function choice")
    
