# Request user input to either print previous calculations from a file or perform a new calculation and save it to the file.
user_choice=str(input("Do you wish to print or perform a calculation - choose (print) or (perform): "))
# Open the file in read or append mode based on user choice
# Handle user choice for printing 
if user_choice == "print":
    # Open the file in read mode and print its contents
    with open ("equations.txt", 'r',encoding='utf-8') as f:
        print("Printing calculations from equations.txt")
        contents = f.readlines()
        for line in contents:
            print(line.strip())
# Handle user choice for performing calculation
elif user_choice == "perform":
    # Open the file in append mode and perform calculation
    with open("equations.txt",'a',encoding='utf-8') as f:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+,-,*,/):")
        num2 = float(input("Enter the second number:"))
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1/num2
            else:
                result = "Error: Division by zero"
        else: 
            result = "Error: Invalid Operator"
        # Write the calculation result to the file
        f.write(f"The result of {num1} {operator} {num2} is: {result}\n")
        print(f"Calculation performed and written to equations.txt") 

            