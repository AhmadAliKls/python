import random

def gameplay(max_num):
    num = random.randint(1, max_num)
    count = 0
    while count < 3:
        val = input(f"Enter your guess from 1-{max_num}: ")
        count += 1
        try:
            value = int(val)
        except ValueError:
            print("Enter a valid integer value")
            continue

        if value == num:
            print("Wow! Correct Guess")
            print("Hurrah!! You guessed in just", count, "tries")
            break
        elif value < num:
            print("Guess is shorter, make a bigger guess--")
        else:
            print("Guess is bigger, make a smaller guess--")
        print("Your guess count is", count)
    else:
        print("You Lost!! The correct number was", num)

while True:
    play_game = input("Want to play game (y/n): ")
    if play_game.lower() == "y":
        level = input("Enter level easy(e)/normal(n)/hard(h): ")
        if level == "e":
            gameplay(10)
        elif level == "n":
            gameplay(50)
        elif level == "h":
            gameplay(100)
        else:
            print("Invalid level choice")
        print("----Game Over----")
    else:
        print("As your wish!!")
        break
