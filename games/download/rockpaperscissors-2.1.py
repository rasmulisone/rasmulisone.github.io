import random
print("Rock Paper Scissors 2.1")
print("(C) 2018 Rasmulisone Games")
print("")
print("r = rock, p = paper, s = scissors")
print("")
while True:
    while True:
        player = 0
        computer = 0
        iTimes = input("Times: ")
        if iTimes == ("exit"):
            quit()
        try:
            times = int(iTimes)
        except ValueError:
            print("Type a number!")
            break
        timesdone = 0
        choice = ("")
        while True:
            choice_ = input("Choice: ")
            if choice_ == ("r"):
                choice = ("rock")
            elif choice_ == ("p"):
                choice = ("paper")
            elif choice_ == ("s"):
                choice = ("scissors")
            elif choice_ == ("exit"):
                break
            else:
                print("Type 'r', 'p' or 's'")
                break
            rpc = random.choice(['rock', 'paper', 'scissors'])
            print(rpc)
            if choice == ("rock"):
                if rpc == ("rock"):
                    print("Tie!")
                elif rpc == ("paper"):
                    print("You lost!")
                    computer += 1
                elif rpc == ("scissors"):
                    print("You won!")
                    player += 1
            elif choice == ("paper"):
                if rpc == ("rock"):
                    print("You won!")
                    player += 1
                elif rpc == ("paper"):
                    print("Tie!")
                elif rpc == ("scissors"):
                    print("You lost!")
                    computer += 1
            elif choice == ("scissors"):
                if rpc == ("rock"):
                    print("You lost!")
                    computer += 1
                elif rpc == ("paper"):
                    print("You won!")
                    player += 1
                elif rpc == ("scissors"):
                    print("Tie!")
            timesdone += 1
            print(str(player) + "-" + str(computer))
            print("")
            if timesdone >= times:
                if player == computer:
                    times += 1
                if timesdone == times:
                    if player < computer:
                        print("YOU LOST!")
                    elif player > computer:
                        print("YOU WON!")
                    break
