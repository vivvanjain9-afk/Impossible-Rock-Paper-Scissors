computer = ""
x = 0
user_choice = input("Enter your choice, rock, paper, or scissors:")
if user_choice == "rock" or user_choice == "Rock" or user_choice == "ROCK":
    computer = "paper"
    print("The computer chose:" + computer)
    print("You chose:" + user_choice)
    print("The computer [always] wins!")
elif user_choice == "paper" or user_choice == "Paper" or user_choice == "PAPER":
    computer = "Scissors"
    print("The computer chose:" + computer)
    print("You chose:" + user_choice)
    print("The computer [always] wins!")
elif user_choice == "scissors" or user_choice == "Scissors" or user_choice == "SCISSORS":
    computer = "rock"
    print("The computer chose:" + computer)
    print("You chose:" + user_choice)
    print("The computer [always] wins!")
elif user_choice == "win" or user_choice == "Win" or user_choice == "WIN":
    print("Finally, you figured out the forbidden word, you won")
else:
    print("Invalid choice try again")
if x == 10:
    print("So you see, you can never win, unless you use the forbidden method)")
if x == 20:
    print("The forbidden word is win")
x = x + 1

