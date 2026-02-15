
# Store corrent 
correct_name = "John"
incorrect_name = []

while True:
    # Use strip and lower case function for case insensitivity
    user_input = input("Enter your name: ").strip().lower()
    if user_input == correct_name.lower():
        break
    incorrect_name.append(user_input)
print(f"Incorrect names: {incorrect_name}")


