def add(number1, number2):
    # adja vissza az összeget
    return number1 + number2

def subtract(number1, number2):
    # adja vissza a különbséget
    return number1 - number2


def multiply(number1, number2):
    # adja vissza a szorzatot
    return number1 * number2

def divide(number1, number2):
    # adja vissza a hányadst
    return number1 / number2

first_number = float(input("Give me a number: "))
second_number = float(input("Give me another number: "))
operation = input("Choose an operation (+, -, *, /)").strip()

if operation == "+" :
    print(add(first_number, second_number))
elif operation == "-":
    print(subtract(first_number,second_number))
elif operation == "*":
    print(multiply(first_number, second_number))
elif operation == "/":
    if second_number == 0:
        print("You cannot divide by zero.")
    else:
        print(divide(first_number,second_number))
else:
    print("Invalid operation.")