def convert_string_case(text):
    # Convert to uppercase
    uppercase_text = text.upper()
    
    # Convert to lowercase
    lowercase_text = text.lower()
    
    return uppercase_text, lowercase_text

# Example usage
original_string = "Hello, World! Welcome to Python."

upper, lower = convert_string_case(original_string)

print(f"Original String: {original_string}")
print(f"Uppercase:     {upper}")
print(f"Lowercase:     {lower}")
