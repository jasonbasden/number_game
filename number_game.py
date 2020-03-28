import random

ranNum = random.randint(0,10)

userNum = int(input("What is your number?: "))

ranNum != userNum

while True:
    if(ranNum > userNum):
        print("Your number is lower, guess again!")
        userNum = int(input("What is your number?: "))
        break
    else:
        print("Your number is hight, guess again!")
        userNum = int(input("What is your number?: "))
        break
    if(ranNum == userNum):
        print("Guessed the number!" + ranNum)
        break


