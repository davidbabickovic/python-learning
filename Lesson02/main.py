

secret_number = 7
attempts = 1

guessed_number =int(input("Guess the secret number: "))

while guessed_number != secret_number:
    if guessed_number < secret_number:
        print("Too low!")

    elif guessed_number > secret_number:
        print("Too high!")

    attempts += 1
    guessed_number =int(input("Guess the secret number: "))
print(f"Congratulations! You found it in {attempts} attempts.")