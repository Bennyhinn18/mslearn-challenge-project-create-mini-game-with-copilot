import random

def get_player_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ")
    return choice.lower()

   

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" or player_choice == "1") and computer_choice == "scissors" or \
         (player_choice == "paper" or player_choice == "2") and computer_choice == "rock" or \
         (player_choice == "scissors" or player_choice == "3") and computer_choice == "paper":
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(player_choice, computer_choice))
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes" and play_again.lower() != "y" and play_again.lower() != "1":
            break

play_game()
