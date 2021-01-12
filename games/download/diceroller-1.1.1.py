import random

def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print("Dice Roller for Python 3 - version 1.1.1")
print("(C) 2021 Rasmulisone Games")
print("")
print("For average result mode type 'avg'")
print("To exit type 'exit'")
print("")
while True:
    dice_ = input("Amount of dice: ")
    if isNumber(dice_):
        dice = int(dice_)
        total = 0
        for i in range(dice):
            result = random.randint(1, 6)
            print(result)
            total += result
        if dice != 1:
            print("Total: " + str(total))
    elif dice_ == ("exit"):
        exit()
    elif dice_ == ("avg"):
        dice_ = input("Dice: ")
        times = input("Times: ")
        if isNumber(dice_) & isNumber(times):
            dice = int(dice_)
            total = 0
            tot_total = 0
            for i in range(int(times)):
                for i in range(dice):
                    result = random.randint(1, 6)
                    print(result)
                    total += result
                if dice != 1:
                    print("Total: " + str(total))
                tot_total += total
                total = 0
            print("")
            print("Total: " + str(tot_total))
            avg = (tot_total / int(times))
            print("Average result: " + str(avg))
            print("Theoretical average result: " + str(3.5 * dice))
        else:
            print("Type numbers!")
    else:
        print("Type a number!")
