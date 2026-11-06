import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\n Choose rock, paper, or scissors (or quit): ").lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer = random.choice(choices)

    print("you chose:", user)
    print("computer chose:", computer)

    if user == computer:
        print("It's a Tie! ")

    elif user == "rock" and computer == "scissors" : 
        print("You win!")

    elif user == "paper" and computer == "rock":
        print("You Win !")

    elif user == "scissors" and computer == "paper":
        print("You Win!")

    else:
        print("YOU LOOSEEE! ")                      
