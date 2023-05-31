import random

print("Welcome to the Guess the Number Game!")

number = random.randint(1, 100)
guesses_taken = 0

while True:
    guess = int(input("Enter your guess (between 1 and 100): "))
    guesses_taken += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number in", guesses_taken, "attempts.")
        break
