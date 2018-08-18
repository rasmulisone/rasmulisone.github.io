import random

def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print("Dice Roller for Python - version 1.0")
print("(C) 2018 Rasmulisone Games")
print("")
while True:
    dice_ = input("Amount of dice: ")
    if isNumber(dice_):
        dice = int(dice_)
        max = dice * 6
        result = random.randint(dice, max)
        print(result)
    elif dice_ == ("exit"):
        exit()
    else:
        print("Type a number!")