# lab4.2_guess2.py
# Prompt a use to guess a number until the user guesses a predefined number.
# If the number is too high or low, tell the user. 
# Author: Nichola Walsh

import random

number_to_guess = random.randint(1,10)

guess = int(input("Please guess a number: "))
print ("Random number is {}". format (number_to_guess))

while guess != number_to_guess:
    if guess < number_to_guess:
        print ("Too low.")
    else:
        print ("Too high.")
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was", number_to_guess)