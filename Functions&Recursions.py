
names = ["Alice", "Bob", "Charlie", "Diana"]

def len_list(lst):
    length = len(lst)
    return length 
print(len_list(names))

#end 

def print_list(lst):
    return lst
print(print_list(names))    


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(factorial(6))  

def convert(n):
    pkr = n * 289.5
    return pkr

pkr_amount = convert(100)
print(pkr_amount)

num1 = int(input("Enter a number: "))
def specs(num):
    if num % 2 == 0 :
        return "Even"
    else:
        return "Odd"
print(specs(num1))

num2 = int(input("Enter a number: "))
def recursive_sum(n):
    return 0 if n == 0 else n + recursive_sum(n - 1)
print(recursive_sum(num2))

num = [1, 2, 3, 4, 5]
def all_elements(lst):
    return lst if len(lst) == 1 else [lst[0]] + all_elements(lst[1:])
print(all_elements(num))

