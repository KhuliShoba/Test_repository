# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

 
print ("Welcome to the error program") # SyntaxError: Missing parentheses in call to 'print'.
print ("\n") # SyntaxError: missing parentheses and incorrect indentation 

    # Variables declaring the user's age, casting the str to an int, and printing the result
age = ("24 years old %") # SyntaxError:incorrect indentation; unidentifiable variable 'age_Str'; missing parenthesis  
age = int(24) # SyntaxError:incorrect indentation; age string not defined 
print(f"I'm {age} years old.") #  SyntaxError: incorrect indentation; can only concatenate str (not "int") to 'str'

    # Variables declaring additional years and printing the total years of age
years_from_now = int(3)  #  SyntaxError: incorrect indentation casting the 'str' to an 'int'
total_years = age + years_from_now #  SyntaxError: incorrect indentation; TypeError: unsupported operand type(s) for +: 'int' and 'str'
answer_years = total_years
print(f"The total number of years: {answer_years} ") # SyntaxError: Missing parentheses in call to 'print'#

# Variable to calculate the total number of months from the given number of years and printing the result
number_years = int(12)
total_months = total_years * number_years # SyntaxError: total not defined 
print (f"In 3 years and 6 months, I'll be {total_months} months old") # SyntaxError: Missing parentheses in call to 'print'. 

#HINT, 330 months is the correct answer

