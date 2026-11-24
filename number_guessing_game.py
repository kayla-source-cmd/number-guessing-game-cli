import random

secret_number = random.randint(1, 10)
attempts = 0

guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed correctly!")
        print(f"You guessed it in {attempts} attempts!")

    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")