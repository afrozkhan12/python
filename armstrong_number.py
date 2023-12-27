def is_armstrong(num):

  original_num = num
  sum_of_digits = 0

  # Extract digits and raise them to the power of number of digits
  while num > 0:
    digit = num % 10
    sum_of_digits += digit ** len(str(original_num))
    num //= 10

  # Check if the sum of digits is equal to the original number
  return sum_of_digits == original_num

# Example usage
number = int(input("enter any number : ")) #153

if is_armstrong(number):
  print(f"{number} is an Armstrong number!")
else:
  print(f"{number} is not an Armstrong number.")