#This imports the random number.
import random

print("Guessing Game")
print("By: CallMeSirEntertainment\n")
#This asks if you want to play, then starts the game if you type y.
play_again_input = input("Would you like to play? (y/n) ")
if play_again_input.lower() == "y":
        play_again = True
else:
    play_again = False
    print("\nWhy did you run this program then?")

while play_again:
    #This asks for your age, then suggests a difficulty based on it.
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
    #This asks what difficulty you would like to play on.
    level = input("Choose a level of difficulty: (easy, normal, hard, insane, impossible)\n")
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
    #This tells you the max number using the max_number variable.
    print(f"\nI'm thinking of a number between 1 and {max_number}.")
    tries = 10
    print(f"You have {tries} tries to guess the number.")
    number = random.randint(1, max_number)
    #This tests for how many tries you have left. If not zero, it prompts you to guess again.
    for i in range(tries):
        guess = int(input("\nEnter your guess: "))

        if guess < number:
            print("\nToo low. Try again.")
        elif guess > number:
            print("\nToo high. Try again.")
        else:
            #This tells you how many tries you took to guess the number.
            print(f"\nCongratulations! You guessed the number in {i+1} tries.")
            break
    else:
        #This tells you the number if you didn't guess it.
        print(f"\nSorry, you ran out of tries. \nThe number was {number}.")
    #This asks if you want to play again, and breaks the loop if you type n.
    play_again_input = input("\nWould you like to play again? (y/n) ")
    if play_again_input.lower() == "n":
        play_again = False
        print("\nThank you for playing!")
