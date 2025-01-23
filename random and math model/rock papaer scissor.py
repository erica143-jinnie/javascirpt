import random
while true:
    user_action=input("Enter a choice(rock,paper,scissors):")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action},computer chose {computer_action}.n")
