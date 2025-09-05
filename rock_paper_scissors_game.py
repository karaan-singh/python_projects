import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    rounds = 5

    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Best of 5 rounds. Type 'quit' anytime to exit.\n")

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        user_choice = input("Enter rock, paper, or scissors: ").lower()

        if user_choice == "quit":
            print("Game ended early. Thanks for playing! 😊")
            break

        if user_choice not in options:
            print("Invalid choice! Try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie! 😐")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round! 🎉")
            user_score += 1
        else:
            print("Computer wins this round! 🤖")
            computer_score += 1

        print(f"Score: You {user_score} - {computer_score} Computer")

    # Final Result
    print("\n🏆 Final Result:")
    if user_score > computer_score:
        print("🎉 Congratulations, you win the game!")
    elif user_score < computer_score:
        print("🤖 Computer wins the game! Better luck next time.")
    else:
        print("😐 It's a tie overall!")

rock_paper_scissors()