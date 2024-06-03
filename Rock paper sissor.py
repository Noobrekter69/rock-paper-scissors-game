import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        computer_choice = random.choice(choices)
        player_choice = None

        while player_choice not in choices:
            player_choice = input("Enter rock, paper, or scissors: ").lower()
            if player_choice not in choices:        
                print("Please choose either rock, paper, or scissors!")

        print(f"Computer chose: {computer_choice}")
        print(f"You chose: {player_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

        user = input("Do you want to play again? (y/n): ").lower()
        if user != 'y':
            print("Thanks for playing!")
            break

rock_paper_scissors()
