# Request the user to enter three different integers#
number1=int(input("Enter first integer number: "))
number2=int(input("Enter second integer number: "))
number3=int(input("Enter third integer number: "))

# Print the all 3 integers#
print("First number is ",number1)
print("Second number is ",number2)
print("Third number is ",number3)

# Calculate the sum of all numbers#
sum=number1+number2+number3

# Print the sum of all numbers# 
print("The sum of all the numbers is ",sum)

# The first number minus the second number#
subtract=(number1-number2)

# Print subtract calculation#
print(number1," minus ",number2 ,"is",subtract)

# Multiply the third number by the second number#
multiply=(number3*number2)

# Print the multiply calculation# 
print(number3, "mutiply" ,number2," is",multiply)

# Calculate the sum of all three numbers and divide by the third number#
expression1=(sum/number3)

# Print the sum of all numbers divided by the third number#
print("The sum of all numbers divided by",number3,"is" ,expression1)
