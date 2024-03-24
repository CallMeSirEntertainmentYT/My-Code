import random as rand
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
    wait_time1 = rand.randint(1,4)
    wait_time2 = rand.randint(1,4)
    wait_time3 = rand.randint(1,4)
    wait_time4 = rand.randint(1,4)
    print("\nWhy did you run this program then?")
    time.sleep(wait_time1)
    print("Are you serious?")
    time.sleep(wait_time2)
    print("You're just going to give up?")
    time.sleep(wait_time3)
    print("AT A GUESSING GAME?")
    time.sleep(wait_time4)
    print("Fine.")
    time.sleep(2)
    sys.exit()
while play_again:
    age = None
    while age is None:
        age = input("Type your age to see a recommended difficulty, or type n to refuse.\n")
        if age.lower() == "n":
            break
        try:
            age = int(age)
        except ValueError:
            print("Invalid input. Please enter a number or 'n'.")
            age = None
            continue
        if age >= 14:
            print("Insane is your recommended difficulty level.")
        elif age >= 10:
            print("Hard is your recommended difficulty level.")
        elif age >= 7:
            print("Normal is your recommended difficulty level.")
        elif age <= 6:
            print("Easy is your recommended difficulty level.")
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
    special_numbers = [69, 420, 21]
    number = rand.randint(1, max_number)
    if number in special_numbers:
        print("Haha, funny number.")
    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    print(f"You have {tries} tries to guess the number.")
    for i in range(tries):
        guess = input("\nEnter your guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
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
            time.sleep(3)
            os.remove(sys.argv[0])
            sys.exit()
    play_again_input = input("\nWould you like to play again? (y/n) ")
    if play_again_input.lower() == "n":
        play_again = False
        print("\nThank you for playing!")
        time.sleep(3)
        sys.exit()
