# Import the random module to generate random choices for the computer
import random

# Function to get the user's choice
def get_user_choice():
    # Prompt the user to enter their choice
    user_choice = input("Choose rock, paper, or scissors: ")
    # Return the user's choice
    return user_choice

# Function to get the computer's choice
def get_computer_choice():
    # Define the possible choices
    choices = ["rock", "paper", "scissors"]
    # Let the computer make a random choice
    computer_choice = random.choice(choices)
    # Return the computer's choice
    return computer_choice

def get_result(user_choice, computer_choice):
    game_rules = {
        'rock': {'rock': 'tie', 'paper': 'computer', 'scissors': 'user'},
        'paper': {'rock': 'user', 'paper': 'tie', 'scissors': 'computer'},
        'scissors': {'rock': 'computer', 'paper': 'user', 'scissors': 'tie'}
    }
    return game_rules[user_choice][computer_choice]

def update_scores(result, user_score, computer_score):
    if result == 'user':
        user_score += 1
    elif result == 'computer':
        computer_score += 1
    return user_score, computer_score

def main(user_choice, computer_choice):
    user_score = 0
    computer_score = 0

    if user_choice in ['rock', 'paper', 'scissors']:
        result = get_result(user_choice, computer_choice)
        user_score, computer_score = update_scores(result, user_score, computer_score)
        print(f"Result: {result.capitalize()}")
    else:
        print("That's not a valid choice!")

    print(f"Score: You - {user_score}, Computer - {computer_score}")
    return user_score, computer_score
# Check if this script is the main module
if __name__ == "__main__":
    # Initialize the play again variable
    play_again = 'y'
    # Keep playing as long as the user wants to play again
    while play_again.lower() == 'y':
        # Initialize the win counters
        user_wins = 0
        computer_wins = 0
        # Keep playing rounds until someone wins 2 rounds
        while user_wins < 2 and computer_wins < 2:
            # Get the user's choice
            user_choice = get_user_choice()
            # Get the computer's choice
            computer_choice = get_computer_choice()
            # Print the computer's choice
            print(f"The computer chose: {computer_choice}")
            # Play the round
            user_score, computer_score = main(user_choice, computer_choice)
            # Update the win counters based on the round result
            if user_score > computer_score:
                user_wins += 1
            elif computer_score > user_score:
                computer_wins += 1
            # Print the round scores
            print(f"Round Score: You - {user_wins}, Computer - {computer_wins}")
        # Print the game result
        if user_wins > computer_wins:
            print("You won the game!")
        else:
            print("The computer won the game!")
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ")