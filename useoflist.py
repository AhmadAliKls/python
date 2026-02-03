names = ["Ahmad", "Ali", "Hassam", "Azan", "Hammad", "Hamza"]

def add_name(name_to_add):
    names.append(name_to_add)
    print(f"{name_to_add} has been added successfully!")

def remove_name(name_to_remove):
    if name_to_remove in names:
        names.remove(name_to_remove)
        print(f"{name_to_remove} has been removed!")
    else:
        print("Error: Name not found in the list.")

def access_list():
    print("📋 Current list:", names)

def clear_list():
    names.clear()
    print("The list is now empty!")

def remove_last_element():
    if names:
        removed = names.pop()
        print(f"{removed} was removed. Current list: {names}")
    else:
        print("Error: List is already empty.")

def remove_first_element():
    if names:
        removed = names.pop(0)
        print(f"{removed} was removed. Current list: {names}")
    else:
        print("Error: List is already empty.")

condition = True
while condition:
    print("\n--- MENU ---")
    print("1. Add name(s)")
    print("2. Remove a name")
    print("3. Access list")
    print("4. Clear list")
    print("5. Remove last element")
    print("6. Remove first element")
    print("7. Quit")
    
    choice = input("Choose an option (1-7): ")
    
    if choice == "1":
        try:
            no_of_names = int(input("Enter number of names to add = "))
            for i in range(no_of_names):
                get_name = input("Enter name to add = ")
                add_name(get_name)
            access_list()
        except ValueError:
            print("Error: Please enter a valid number.")
    elif choice == "2":
        get_name = input("Enter name to remove = ")
        remove_name(get_name)
    elif choice == "3":
        access_list()
    elif choice == "4":
        clear_list()
    elif choice == "5":
        remove_last_element()
    elif choice == "6":
        remove_first_element()
    elif choice == "7":
        print("Final list state:", names)
        print("Exiting program. Goodbye!")
        condition = False
    else:
        print("Error: Invalid input.")
