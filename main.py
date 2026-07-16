

name = "User"
age = 20
goal = "Programmer"
#print("hey my name is: "+name)
#print("i am "+str(age)+" years old")
#print("i want to be a "+goal)

#print(f"my name is {name}")
#print(f"i am {age} years old")
#print(f"i want to be a {goal}")

#name = input("Whats your name? :")
#age = input("How old are you? :")
#print(f"Hello {name} !")
#print(f"Next year you will be {int(age)+1} years old.")

age = int(input("how old are you? "))
if age < 18:
    print("You are underage.")
else:
    print("You are an adult.")