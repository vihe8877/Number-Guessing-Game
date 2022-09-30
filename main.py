#Make a number guessing game. 
#Generate a random number from 1 - 100 and ask the user to guess it. 
#To help them guess more accurately, 
#tell the user if their guess was too high or too low after each incorrect guess.
import random
ran_num = random.randrange(1,101)
answer = ""
count = 0
play = True

while answer!= ran_num:
  answer = int(input("Guess the number: (1 - 100)\n"))
  if answer == ran_num:
    print("\nCongrats! You guessed the number!\n")
    print("It took you", count, "tries to guess the number!\n")
  if answer > ran_num:
    print("The number is smaller than that.\n")
    count = count + 1
  if answer < ran_num:
    print("The number is larger than that.\n")
    count = count + 1

#Looping until user wants to quit
while play:
  anotherGame = input("Would you like to play again? (yes/no)\n")
  ran_num = random.randrange(1,101)
  answer = ""
  count = 0
  
  if anotherGame.lower() == "yes" or anotherGame.lower() == "y":
    play = True
    while answer!= ran_num:
      answer = int(input("Guess the number: (1 - 100)\n"))
      if answer == ran_num:
        print("\nCongrats! You guessed the number!\n")
        print("It took you", count, "tries to guess the number!\n")
      if answer > ran_num:
        print("The number is smaller than that.\n")
        count = count + 1
      if answer < ran_num:
        print("The number is larger than that.\n")
        count = count + 1

  elif anotherGame.lower() == "no" or anotherGame.lower() == "n":
    play = False #if user puts no or n, quit game