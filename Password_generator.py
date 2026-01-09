import random
import string

password_len = input("Enter the length of password you want to generate: ")

try:
    value = int(password_len)
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if value < 4:
    print("Password length should be at least 4 for security.")
    exit()

characters = string.ascii_letters + string.digits + string.punctuation

# Ensure strong password: at least one of each type
password = (
    random.choice(string.ascii_lowercase) +
    random.choice(string.ascii_uppercase) +
    random.choice(string.digits) +
    random.choice(string.punctuation)
)

# Fill the rest randomly
password += "".join(random.choice(characters) for i in range(value - 4))

# Shuffle to avoid predictable order
password = "".join(random.sample(password, len(password)))

print("Generated password:", password)
