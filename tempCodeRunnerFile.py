#Documentation
#this version of the dice game not only provides the random number produced, but also provides a diagram of it 
#import random 
import random

#function which produces a random between 1 and 6
def dice(user_input):
    if user_input == "d":
            #generate a random integer
            random_dice = random.randint(1,6)
            return random_dice; 
    
           
          

print("Hello Player")
while True:
    user_input = input(str("Enter D to output random number from Dice "))
    #break incase Anything but D is pressed 
    if user_input != "d":
         break
    system_output = dice(user_input)
    print(f"You rolled a",system_output)
    if system_output == 1:
         print("-------")
         print("|     |")
         print("|  o  |")
         print("|     |")
         print("-------")
    elif system_output == 2:
         print("-------")
         print("|o    |")
         print("|     |")
         print("|    o|")
         print("-------")
    elif system_output == 3:
         print("-------")
         print("|o    |")
         print("|  o  |")
         print("|    o|")
         print("-------")
    elif system_output == 4:
         print("-------")
         print("|o   o|")
         print("|     |")
         print("|o   o|")
         print("-------")
    elif system_output == 5:
         print("-------")
         print("|o   o|")
         print("|  o  |")
         print("|o   o|")
         print("-------")
    elif system_output == 6:
         print("-------")
         print("|o   o|")
         print("|o   o|")
         print("|o   o|")
         print("-------")
    else:
         print("invalid dice number")
    

    






