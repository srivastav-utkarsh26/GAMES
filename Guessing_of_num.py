import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
guesses = 0
user_guess = 0

print("=== The Perfect Guess Game ===")
print("Guess a number between 1 and 100")

# Keep asking until the user gets it right
while user_guess != secret_number:
    user_guess = int(input("Enter your guess: "))
    guesses = guesses + 1

    if user_guess > secret_number:
        print("Lower number please!")
    elif user_guess < secret_number:
        print("Higher number please!")

print("\nCongratulations! You guessed it right!")
print("Number of guesses taken:", guesses)