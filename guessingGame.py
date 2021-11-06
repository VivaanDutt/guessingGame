import random

ranNumber = random.randint(1,9)
attempts = 5

print('Number Guessing Game')



while attempts > 0:
    numberInput = int(input("Guess a Number (between 1 and 9)"))
    if numberInput < ranNumber:
        print("Your guess was too low: Guess a number higher than " , numberInput)
    elif numberInput > ranNumber:
        print("Your guess was too high: Guess a number lower than " , numberInput)
    else:
        print("Congratulations, YOU WON!!!")
        break
    attempts -= 1
     
if attempts == 0:
    print("You lose!!! The number was " , ranNumber)
    print("Try again!!") 

