# lab4.2_average.py
# Program keeps reading numbers until the user enters a 0.
# Then the program prints out each of the numbers entered and gets the average using a list. 
# Author: Nichola Walsh


numbers = []
number = int(input("Enter a number (0 to quit): "))

while number != 0:
    numbers.append(number)

    number = int(input("enter another (0 to quit)"))

for value in numbers:
    print (value)

average = float (sum(numbers))/len(numbers)
print (f"The average is {average}")


