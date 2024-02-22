import random
import os
import sys
import time

print("Guessing Game")
print("By: CallMeSirEntertainment\n")
play_again_input = input("Would you like to play? (y/n) ")
if play_again_input.lower() == "y":
        play_again = True
else:
    play_again = False
    print("\nWhy did you run this program then?")

while play_again:
    age = None
    while age is None:
        age = input("Type your age to see a recommended difficulty, or type n to refuse.\n")
        if age == "n":
            break
        age = int(age)
        if age >= 14:
            print("Insane is your recommended difficulty level.")
        elif age >= 10:
            print("Hard is your recommended difficulty level.")
        elif age >= 7:
            print("Normal is your recommended difficulty level.")
        elif age <= 6:
            print("Easy is your recommended difficulty level.")
            break
    level = input("Choose a level of difficulty: (easy, normal, hard, insane, impossible)\n")
    tries = 10
    safe_mode_input = input("Would you like to enable safe mode? Safe mode prevents the game from deleting itself if you fail to guess the number in ten tries. (y/n)\n")
    if safe_mode_input.lower() == "y":
        safe_mode = True
    else:
        safe_mode = False
    if level == "easy":
        max_number = 50
    elif level == "normal":
        max_number = 100
    elif level == "hard":
        max_number = 250
    elif level == "insane":
        max_number = 500
    elif level == "impossible":
        max_number = 1000
    else:
        print("Invalid level of difficulty. Please choose again.")
        continue
    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print(f"You have {tries} tries to guess the number.")
    number = random.randint(1, max_number)
    for i in range(tries):
        guess = int(input("\nEnter your guess: "))

        if guess < number:
            print("\nToo low. Try again.")
        elif guess > number:
            print("\nToo high. Try again.")
        else:
            print(f"\nCongratulations! You guessed the number in {i+1} tries.")
            break
    else:
        print(f"\nSorry, you ran out of tries. \nThe number was {number}.")
        if not safe_mode:
            print("\nDeleting the game as you failed to guess the number in ten tries.")
            time.sleep(5)  # Wait for 5 seconds
            os.remove(sys.argv[0])
            sys.exit()
    play_again_input = input("\nWould you like to play again? (y/n) ")
    if play_again_input.lower() == "n":
        play_again = False
        print("\nThank you for playing!")

