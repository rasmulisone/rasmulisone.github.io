import random

again = ("")

while True:
    valinta = random.choice(['rock', 'paper', 'scissors'])
    print(valinta)
    again = input("Again? (y/n): ")
    if again == "n":
        quit()