# Sum of all odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_sum = sum(x for x in numbers if x % 2 != 0)
print(f"Sum of odd numbers: {odd_sum}")