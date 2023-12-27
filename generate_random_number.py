import random

# Generate a random float between 0.0 and 1.0
random_float = random.random()
print(f"Random float: {random_float}")

# Generate a random integer between 1 and 10 (inclusive)
random_int = random.randint(1, 10)
print(f"Random integer (1-10): {random_int}")

# Generate a random choice from a list
names = ["Alice", "Bob", "Charlie"]
random_name = random.choice(names)
print(f"Random name from list: {random_name}")


random_integer = random.randint(1,100)

print(f"Random Integer from 0 to 100: {random_integer}")