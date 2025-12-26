from typing import List

names: List[str] = []

def add_name(new_name: str) -> None:
    """Add a trimmed name to the list."""
    names.append(new_name.strip())

def get_names() -> List[str]:
    """Return a copy of the current names list."""
    return names.copy()

def clear_names() -> None:
    """Remove all names from the list."""
    names.clear()

def prompt_int(prompt: str) -> int:
    """Prompt repeatedly until the user enters a non-negative integer."""
    while True:
        resp = input(prompt).strip()
        if resp == "":
            print("Please enter a number (or 0).")
            continue
        try:
            n = int(resp)
            if n < 0:
                print("Please enter a non-negative number.")
                continue
            return n
        except ValueError:
            print("That's not a valid number. Please try again.")

def prompt_yes_no(prompt: str) -> bool:
    """Prompt until user answers yes or no. Returns True for yes."""
    while True:
        resp = input(prompt + " [y/n]: ").strip().lower()
        if resp in ("y", "yes"):
            return True
        if resp in ("n", "no"):
            return False
        print("Please answer 'y' or 'n' (yes or no).")

def main() -> None:
    count = prompt_int("How many names do you want to add? ")
    if count == 0:
        print("You did not add any names to the list.")
        return

    for i in range(count):
        input_name = input(f"Enter name #{i+1}: ")
        add_name(input_name)

    if prompt_yes_no("Do you want to see the list items you added?"):
        print("Current names in the list:", get_names())
    else:
        print("Okay — not showing the list.")

if __name__ == "__main__":
    main()
