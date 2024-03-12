import random as rand
import system as sys
import time
print("Welcome to the dice game!\n You will roll a die and an AI will also roll a die. Whoever has the highest number wins!")
play = input("Would you like to play? (y/n)\n")
if play == "y":
    playing = True
    while playing == True:
        roll = input("Roll the die? (y/n)\n")
        if roll == "y":
            player_roll = rand.randint(1,6)
            ai_roll = rand.randint(1,6)
            print("Player rolled a",player_roll,"\nAI rolled a",ai_roll)
            if ai_roll > player_roll:
                print("AI wins!")
            elif ai_roll < player_roll:
                print("Player wins!")
            else:
                print("It's a tie!")
        elif roll == "n":
            print("Goodbye!")
            time.sleep(2)
            sys.exit
            break
        else:
            print("Invalid, please enter either y or n.")
else:
    print("Goodbye!")
    time.sleep(2)
    sys.exit
