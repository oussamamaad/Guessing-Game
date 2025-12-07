import random

number = random.randint(1, 10)

print("Welcome to the Guessing Game!")
print("I have chosen a number between 1 and 10. Try to guess it!")

guess = int(input("Enter your guess: "))

if guess == number:
    print("Congratulations! You guessed the right number! ")
else:
    print(f"Wrong! The correct number was {number}")
