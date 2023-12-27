import math

# User input for the number
number = float(input("Enter a number: "))

# Use various functions of math module
e_raised_to_number = math.exp(number)
floor_value = math.floor(number)
ceil_value = math.ceil(number)

if number >= 0 and number.is_integer():
    factorial_of_number = math.factorial(int(number))
else:
    factorial_of_number = "Undefined for negative numbers or non-integer values"

square_root_number = math.sqrt(number)
pow_result = math.pow(2, number)  # Example with base 2
cosine_value = math.cos(number)

# Print results with descriptive labels
print(f"e raised to the power of {number}: {e_raised_to_number:.2f}")
print(f"Floor of {number}: {floor_value}")
print(f"Ceiling of {number}: {ceil_value}")
print(f"Factorial of {number}: {factorial_of_number}")
print(f"Square root of {number}: {square_root_number:.2f}")
print(f"2 raised to the power of {number}: {pow_result:.2f}")
print(f"Cosine of {number}: {cosine_value:.2f}")