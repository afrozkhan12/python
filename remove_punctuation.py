import string

def remove_punctuation(input_string):
    # Using string.punctuation to get the set of all punctuation characters
    translator = str.maketrans("", "", string.punctuation)
    
    # Using translate() to remove punctuation
    result = input_string.translate(translator)
    return result

# Example usage:
input_text = "Hello, World! This is an example string with punctuation!!!"
output_text = remove_punctuation(input_text)

print("Original String:")
print(input_text)

print("\nString after removing punctuation:")
print(output_text)