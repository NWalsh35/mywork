# lab4.1_isEven.py
# Ask the user to enter a number and the program tells the user whether the number they entered is even or odd.
# Author: Nichola Walsh

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print(f'{number} is an even number')

else:
    print(f'{number} is an odd number')