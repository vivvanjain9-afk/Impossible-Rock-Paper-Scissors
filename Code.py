computer = range(1,3)
if computer ==1:
    choice = rock
elif computer ==2:
    choice = paper
else:
    choice = scissors
user_choice =input("Enter a choice, rock, paper, or scissors:")
if user_choice == "rock" or "Rock":
    if choice == "rock":
        print("It's a tie")
    elif choice == "paper":
        print("You lost")
    else:
        print("You won")
elif user_choice == "paper" or "Paper":
    if choice == "rock":
        print("You won")
    elif choice == "paper":
        print("It's a tie")
    else:
        print("You lost") 
elif user_choice == "scissors" or "Scissors":
    if choice == "rock":
        print("You lost")
    elif choice == "paper":
        print("You won")
    else:
        print("It's a tie")
else:
    print("Invalid choice")
#this is my project
