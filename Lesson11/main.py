
def intconverter(text) :
    try : 
        number = int(text)
        return number
    except ValueError:
        print("Invalid number")
        return None
        
number1 = None
number2 = None
results = None

while number1 is None:

    number1 = input("Give me the first number ")
    number1 = (intconverter(number1))

while number2 is None:
    number2 = input("Give me the second number ")
    number2 = (intconverter(number2))



try :
    results = number1/number2
except ZeroDivisionError:
     print("You cannot divide by zero!")

if results != None:
    print(f"The result is: {results}")
