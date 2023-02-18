# floor.py
# Take in a float and output an int rounded down.
# Author: Nichola Walsh

import math
number_to_floor = float(input("Enter a float number: "))
floored_number = math.floor(number_to_floor)
print('{} floored is {} '. format(number_to_floor, floored_number))
