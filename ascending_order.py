# # Accept n elements from the user and arrange them in ascending order
n = int(input("Enter the number of elements: "))
arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
arr.sort()
print(f"Elements in ascending order: {arr}")

# def get_elements(n):
#     elements = []
#     for _ in range(n):
#         element = float(input("Enter element: "))  # Assuming input should be numeric
#         elements.append(element)
#     return elements

# def arrange_in_ascending_order(elements):
#     return sorted(elements)

# # Get the number of elements from the user
# n = int(input("Enter the number of elements: "))

# # Get the elements from the user
# user_elements = get_elements(n)

# # Arrange the elements in ascending order
# sorted_elements = arrange_in_ascending_order(user_elements)

# # Display the result
# print("Original elements:", user_elements)
# print("Elements in ascending order:", sorted_elements)
