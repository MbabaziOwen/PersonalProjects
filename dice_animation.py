# Function to print dice faces
def print_dice(number):
    if number == 1:
        print(" ----- ")
        print("|     |")
        print("|  o  |")
        print("|     |")
        print(" ----- ")
    elif number == 2:
        print(" ----- ")
        print("| o   |")
        print("|     |")
        print("|   o |")
        print(" ----- ")
    elif number == 3:
        print(" ----- ")
        print("| o   |")
        print("|  o  |")
        print("|   o |")
        print(" ----- ")
    elif number == 4:
        print(" ----- ")
        print("| o o |")
        print("|     |")
        print("| o o |")
        print(" ----- ")
    elif number == 5:
        print(" ----- ")
        print("| o o |")
        print("|  o  |")
        print("| o o |")
        print(" ----- ")
    elif number == 6:
        print(" ----- ")
        print("| o o |")
        print("| o o |")
        print("| o o |")
        print(" ----- ")
    else:
        print("Invalid dice number!")

# Example usage
import random

dice_roll = random.randint(1, 6)  # Simulating a dice roll
print(f"You rolled a {dice_roll}:")
print_dice(dice_roll)
