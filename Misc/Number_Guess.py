from random import randint

random_number = randint(1, 100)
guesses = 0

while True:
    guess = int(input("Guess a number betweeen 1 and 100: "))

    if guess < random_number:
        print("Too low! Try again.")

    elif guess > random_number:
        print("Too high! Try again.")

    else:
        print(f"Congratulations! You've guessed the number {random_number} in {guesses} guesses!")
        break

    guesses += 1