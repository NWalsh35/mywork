# normalise.py
# Reads in a string and strips leading / trailing spaces. Converts the string to lower case.
# Output the length of the input and output strings. 
# Author: Nichola Walsh

raw_string = input("Please enter a string: ")
normalised_string = raw_string.strip().lower()

length_of_raw_string = len(raw_string)
length_of_normalised_string = len(normalised_string)

print(f"That String normalised is : {normalised_string}")
print(f'We reduced the input string from {length_of_raw_string} to {length_of_normalised_string} characters')

