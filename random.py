import random

user_action = input("Enter a choice (rock,paper,scissor);")
possible_action =["rock","paper","scissor"]
computer_action = random.choice(possible_action)

print(f"\nYou chose {user_action},computer chose {computer_action},\n")

if user_action == computer_action:
         print(f"Both player selected {user_action}. It's a tie!")
elif user_action == "rock":
        if computer_action == "scissor":
           print("rock smashes scissor! You win!")
        else:
           print("paper covers rock!you lose.")
elif user_action == "paper":
        if computer_action == "rock":
           print("paper covers rock! you win!")
        else:
           print("scissor cuts paper;you lose.")
elif user_action == "scissor":
        if computer_action == "paper":
           print("scissor cuts papper!you Win!")
        else:
           print("rock smahes scissor!you lose.")





        
