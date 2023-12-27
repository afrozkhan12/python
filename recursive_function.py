# Algorithm
# if n == 0 base case else: n * function(n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number =int(input("enter any number : ")) 

result = factorial(number)

print(f"the factorial of number {number} is {result}")
