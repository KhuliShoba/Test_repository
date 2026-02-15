# Find the largest number in a list using recursion
# User to input list of numbers, and the function will return the largest number in that list using recursion.
def largest_number(numbers):
    # Base case: if the list is empty, return None
    if not numbers:
        return None
    # Base case: if the list has only one number, return that number
    if len(numbers) == 1:
        return numbers[0]
    # Recursive case: compare the first number with the largest number in the rest of the list
    max_of_rest = largest_number(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest
# Get user input and convert it to a list of integers
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
largest = largest_number(numbers)
if largest is not None:
    print(f"The largest number in the list is: {largest}")
else:    print("The list is empty. No largest number found.")
