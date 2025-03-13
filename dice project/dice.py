#import random 
import random
print("Hello Player")

#Ask for user input 
user_input = input(str("Enter D to output random number from Dice "))

#while loop (infinite)
while True:
    if user_input == "d":
        #generate a random integer
        random_dice = random.randint(1,6)
        print(random_dice)
        break
            
    if user_input == "d":
        #generate a random integer
        random_integer = random.randint(1, 6)
        #print generated float
        print(random_integer) 
        if user_input =="e":
            print("ending game..")
            break

