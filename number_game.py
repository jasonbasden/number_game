import random

ranNum = random.randint(0,10)

userNum = int(input("What is your number?: "))

while ranNum != userNum:
    if(ranNum > userNum):
        print("Your number is lower, guess again!")
    else:
        print("Your number is hight, guess again!")

if(ranNum == userNum):
    print("Guessed the number!" + ranNum)
else: