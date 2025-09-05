import random

print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100 (or type 'quit' to exit): ")
    if guess.lower() == 'quit':
        print("Game exited. Thanks for playing!")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break