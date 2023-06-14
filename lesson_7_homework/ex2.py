# Exercise 2: Guessing game
# Write a program that generates a random number between 1 and 100 and lets the user guess the number. The program should
# provide feedback ("higher" or "lower") until the user guesses the correct number. The program should also keep track of
# the number of guesses it takes for the user to guess correctly.


import random

def guess_number():
    target_number = random.randint(1, 100)
    num_guesses = 0
    guessed_correctly = False

    while not guessed_correctly:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        num_guesses += 1

        if user_guess < target_number:
            print("Higher")
        elif user_guess > target_number:
            print("Lower")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly.")
            guessed_correctly = True

    print(f"It took you {num_guesses} guesses.")

# Start the game
guess_number()
