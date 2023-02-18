# lab4.2_guess1.py
# Prompt a use to guess a number until the user guesses a predefined number.
# Author: Nichola Walsh

number_to_guess = 30

guess = int(input("Please guess a number: "))
while guess != number_to_guess:
    print ("Wrong")
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was", number_to_guess)
