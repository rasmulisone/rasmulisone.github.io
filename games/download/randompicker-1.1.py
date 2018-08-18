import random
print("RandomPicker 1.1 for Python 3")
print("(C) 2017 Rasmulisone Games")
print("")
while True:
    while True:
        iCount = input("Amount of options: ")
        if iCount == ("2") or iCount == ("3") or iCount == ("4") or iCount == ("5") or iCount == ("6") or iCount == ("7") or iCount == ("8") or iCount == ("9") or iCount == ("10") or iCount == ("11") or iCount == ("12") or iCount == ("13") or iCount == ("14") or iCount == ("15"):
            count = int(iCount)
            o1 = input("1: ")
            o2 = input("2: ")
            if count > 2:
                o3 = input("3: ")
                if count > 3:
                    o4 = input("4: ")
                    if count > 4:
                        o5 = input("5: ")
                        if count > 5:
                            o6 = input("6: ")
                            if count > 6:
                                o7 = input("7: ")
                                if count > 7:
                                    o8 = input("8: ")
                                    if count > 8:
                                        o9 = input("9: ")
                                        if count > 9:
                                            o10 = input("10: ")
                                            if count > 10:
                                                o11 = input("11: ")
                                                if count > 11:
                                                    o12 = input("12: ")
                                                    if count > 12:
                                                        o13 = input("13: ")
                                                        if count > 13:
                                                            o14 = input("14: ")
                                                            if count > 14:
                                                                o15 = input("15: ")
                                                                choice = random.choice([o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13, o14, o15])
                                                                print(choice)
                                                                break
                                                            choice = random.choice([o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13, o14])
                                                            print(choice)
                                                            break
                                                        choice = random.choice([o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13])
                                                        print(choice)
                                                        break
                                                    choice = random.choice([o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12])
                                                    print(choice)
                                                    break
                                                choice = random.choice([o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11])
                                                print(choice)
                                                break
                                            choice = random.choice([o1, o2, o3, o4, o5, o6, o7, o8, o9, o10])
                                            print(choice)
                                            break
                                        choice = random.choice([o1, o2, o3, o4, o5, o6, o7, o8, o9])
                                        print(choice)
                                        break
                                    choice = random.choice([o1, o2, o3, o4, o5, o6, o7, o8])
                                    print(choice)
                                    break
                                choice = random.choice([o1, o2, o3, o4, o5, o6, o7])
                                print(choice)
                                break
                            choice = random.choice([o1, o2, o3, o4, o5, o6])
                            print(choice)
                            break
                        choice = random.choice([o1, o2, o3, o4, o5])
                        print(choice)
                        break
                    choice = random.choice([o1, o2, o3, o4])
                    print(choice)
                    break
                choice = random.choice([o1, o2, o3])
                print(choice)
                break
            choice = random.choice([o1, o2])
            print(choice)
        elif iCount == ("exit"):
            quit()
        else:
            print("Type a number from 2 to 15")