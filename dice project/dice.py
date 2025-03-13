#import random 
import random

def dice(user_input):
    if user_input == "d":
            #generate a random integer
            random_dice = random.randint(1,6)
            return random_dice; 
    
           
          

print("Hello Player")
while True:
    user_input = input(str("Enter D to output random number from Dice "))
    if user_input != "d":
         break
    system_output = dice(user_input)
    print(system_output)
    






