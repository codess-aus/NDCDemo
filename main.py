import random

def get_user_choice():
    return input("Choose rock, paper, or scissors: ")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

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