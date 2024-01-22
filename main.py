import random

def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ")
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def main(user_choice, computer_choice):
    user_score = 0
    computer_score = 0
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("The computer wins!")
            computer_score += 1
        else:
            print("You win!")
            user_score += 1
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("The computer wins!")
            computer_score += 1
        else:
            print("You win!")
            user_score += 1
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("The computer wins!")
            computer_score += 1
        else:
            print("You win!")
            user_score += 1
    else:
        print("That's not a valid choice!")
    print(f"Score: You - {user_score}, Computer - {computer_score}")
    return user_score, computer_score

if __name__ == "__main__":
    play_again = 'y'
    while play_again.lower() == 'y':
        user_wins = 0
        computer_wins = 0
        while user_wins < 2 and computer_wins < 2:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"The computer chose: {computer_choice}")
            user_score, computer_score = main(user_choice, computer_choice)
            if user_score > computer_score:
                user_wins += 1
            elif computer_score > user_score:
                computer_wins += 1
            print(f"Round Score: You - {user_wins}, Computer - {computer_wins}")
        if user_wins > computer_wins:
            print("You won the game!")
        else:
            print("The computer won the game!")
        play_again = input("Do you want to play again? (y/n): ")
