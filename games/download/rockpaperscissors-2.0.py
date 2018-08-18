import random
print("Rock Paper Scissors 2.0")
print("(C) 2017 Rasmulisone Games")
print("")

while True:
    player = 0
    computer = 0
    iTimes = input("Times: ")
    if iTimes == ("exit"):
        quit()
    times = int(iTimes)
    timesdone = 0
    while True:
        choice = input("Choice: ")
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
        else:
            print("Type 'rock', 'paper' or 'scissors'")
        timesdone += 1
        print(str(player) + "-" + str(computer))
        if timesdone == times:
            if player == computer:
                times += 1
            if timesdone == times:
                if player < computer:
                    print("YOU LOST!")
                elif player > computer:
                    print("YOU WON!")
                break
            