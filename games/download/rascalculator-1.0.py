import math
print("rasCalculator 1.0")
print("(C) 2018 Rasmulisone Games")
print("")
print("+ - * / exp sqrt %of -%")
while True:
    c_type = input("Calculation type: ")
    if c_type == ("exit"):
        quit()
    elif c_type == ("-%"):
        first = float(input("Number: "))
        percent = float(input("Percent: "))
        one = (first / 100)
        result = (first - one * percent)
        print(result)
    elif c_type == ("%of"):
        first = float(input("Number: "))
        percent = float(input("Percent: "))
        one = (first / 100)
        result = (one * percent)
        print(result)
    elif c_type == ("exp"):
        first = float(input("Number: "))
        exp = float(input("Exponent: "))
        result = math.pow(first, exp)
        print(result)
    elif c_type == ("sqrt"):
        first = float(input("Number: "))
        result = math.sqrt(first)
        print(result)
    elif c_type == ("+"):
        first = float(input("1st number: "))
        second = float(input("2nd number: "))
        result = (first + second)
        print(result)
    elif c_type == ("-"):
        first = float(input("1st number: "))
        second = float(input("2nd number: "))
        print(first)
        print(second)
        result = (first - second)
        print(result)
    elif c_type == ("*"):
        first = float(input("1st number: "))
        second = float(input("2nd number: "))
        result = (first * second)
        print(result)
    elif c_type == ("/"):
        first = float(input("1st number: "))
        second = float(input("2nd number: "))
        result = (first / second)
        print(result)
    else:
        print('Type "+", "-", "*" or "/"')