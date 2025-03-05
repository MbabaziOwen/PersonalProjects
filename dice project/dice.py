#import random 
import random
print("Hello Player")

#Ask for user input 
user_input = input(str("Enter D to output random number from Dice "))
if user_input == "d":
    #generate a random integer
    random_integer = random.randint(1, 6)
    #print generated float
    print(random_integer) 

else:
    print('enter D for random number')



