import random

while True:
    roll = input("Press Enter to roll the dice or type 'quit' to exit: ")
    if roll.lower() == 'quit':
        print("Exiting dice roller.")
        break
    result = random.randint(1, 6)
    print(f"You rolled a {result}!")