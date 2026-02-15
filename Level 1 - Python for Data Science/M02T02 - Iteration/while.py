# Set the counter to 0
i = 0
sum = 0
ave = 0
found = True
while found:
    # Request user to input a number 
    input_num=int(input(" Input any number: "))
   
    # Check the input to ensure it is neither -1 nor 0
    if input_num == -1 or input_num == 0:

        # If input is 0 or -1 print error message 
        print("Input number not valid")

        # Exit the loop
        found = False
        print(f" Last input number: {input_num} Counter: {i} Total: {sum} Average:{ave}") 

    # If number valid move counter once    
    i = i + 1

    # Keep running total of input numbers 
    sum = sum + input_num

    # Calculate the average
    ave = sum/i   