name = []
def add_name(new_name):
    name.append(new_name)
def get_names():
    return name

def clear_names():
    name.clear()

a = input("How many names do you want to add? ")
if a == "0":
    print("You did not add any names to the list")
else:
    for i in range(int(a)):
        input_name = input("Enter a name to add: ")
        add_name(input_name)
    if a != "0":
        ques = input("Do you want to see the list items you added ?")
        if  ques == "yes":
            print("Current names in the list:", get_names())
        else:
            print("On your cammand")    
