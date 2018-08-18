import random
print("Rock Paper Scissors 1.1")
print("(C) 2017 Rasmulisone Games")
print("")
while True:
    rpc = random.choice(['rock', 'paper', 'scissors'])
    print(rpc)
    again = input("Again? (y/n): ")
    if again == "n":
        quit()