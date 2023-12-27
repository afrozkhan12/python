import re

# Check if a string starts and ends with the same character using regex
input_string = input("Enter a string: ")
if re.match(r'^(.).*\1$', input_string):
    print("String starts and ends with the same character.")
else:
    print("String does not start and end with the same character.")