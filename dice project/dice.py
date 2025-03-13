#import random 
import random

def dice(user_input):
    if user_input == "d":
            #generate a random integer
            random_dice = random.randint(1,6)
            print(random_dice)
            return 0; 
    else:
         return -1; 
          

         
          
            
    

print("Hello Player")
while True:
    user_input = input(str("Enter D to output random number from Dice "))
    system_output = dice(user_input)
    print(system_output)






