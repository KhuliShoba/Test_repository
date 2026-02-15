# User to input list of numbers, and the function will return the sum of those numbers using recursion.

def sum_numbers(numbers):
    # Base case: if the list is empty, return 0
    if not numbers:
        return 0
    # Recursive case: add the first number to the sum of the rest of the list
    return numbers[0] + sum_numbers(numbers[1:])    
# Get user input and convert it to a list of integers
user_input = input("Enter a list of numbers separated by spaces: ")
# Get user to input index number to sum up to
index_input = int(input("Enter the index number to sum up to (0-based index): "))
numbers = list(map(int, user_input.split()))
print(f"The sum of the numbers up to index {index_input} is: {sum_numbers(numbers[:index_input + 1])}")