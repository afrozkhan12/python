# Just demonstrate string functions of python


# Example string
example_string = "Python Programming is Fun"

# Using various string functions
uppercase_string = example_string.upper()
lowercase_string = example_string.lower()
capitalized_string = example_string.capitalize()
titlecased_string = example_string.title()
reversed_string = ''.join(reversed(example_string))
length_of_string = len(example_string)
word_list = example_string.split()

# Print results with descriptive labels
print(f"Original String: {example_string}")
print(f"Uppercase String: {uppercase_string}")
print(f"Lowercase String: {lowercase_string}")
print(f"Capitalized String: {capitalized_string}")
print(f"Titlecased String: {titlecased_string}")
print(f"Reversed String: {reversed_string}")
print(f"Length of String: {length_of_string}")
print(f"List of Words: {word_list}")