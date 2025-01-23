import random
playing = True
num = str(random.randint(10,20))
print("I will generate a number from 10 to 20,and you have the guess the number one digit at a time.")
print("The game ends when you get 1 points")
while playing
   guess = input("Give me your best guess \n")
   if num == guess:
      print("You win!")
      print("the number was",num)
      break
   else:
      print("The guess was wrong, Guess again")