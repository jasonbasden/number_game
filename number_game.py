import random

ranNum = random.randint(0,10)

userNum = int(input("What is your number?: "))

while ranNum != userNum:
    if(ranNum > userNum):
        print("Your number is lower, guess again!")
        userNum = int(input("What is your number?: "))
    else:
        print("Your number is higher, guess again!")
        userNum = int(input("What is your number?: "))
if(ranNum == userNum):
    print("You guessed the number!" + str(ranNum))


