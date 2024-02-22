import os
import random
import sys
import time

win_probability = 0.75  # Initial win probability
file_path = os.path.realpath(__file__)

print("DISCLAIMER: This game has a unique feature where it will delete itself from your system if you lose. This means that the Python file you're running will be permanently removed from its directory, which is irreversible. This feature is intended for entertainment purposes and is used to add suspense. By choosing to play, you acknowledge and accept these terms. Do you agree to this? (y/n)")
agree = input()
if agree.lower() != "y":
    print("You chose not to play. Exiting game.")
    sys.exit()

first_play = True

while True:
    if first_play:
        play = input("Do you want to play? (y/n): ")
        first_play = False
    else:
        play = input("Would you like to risk it again? (y/n): ")

    if play.lower() != "y":
        print("Exiting game.")
        break

    if random.random() < win_probability:
        print("You won!")
        win_probability *= 0.95  # Decrease the win probability by 5%
    else:
        print("You lost! The game will now delete itself.")
        time.sleep(5)
        os.remove(file_path)
        sys.exit()
