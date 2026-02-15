# Request the user to input their age & store as integer called age#
age=int(input("Please enter your age: "))
# If the user enter over 100,output: " Sorry your dead."#
if age > 100:
    print("Sorry, your dead. ")
  # If the user is 65, or older output: "Enjoy your retirement!"#
elif age >= 65:
    print("Enjoy your retirement!") 
  # If the user is 40, or over, output: " You're over the hill.#
elif age >= 40:
    print("You're over the hill.") 
# If the user is 21, output: " Congrats on your 21st!"#
elif age == 21:
    print("Congrats on your 21st!") 
# If the user is under 13, output: "You qualify for the kiddie discount."#    
elif age < 13:
    print("You qualify for the kiddie discount.")
# For any other age, output: "Age is but a number"    
else:
    print("Age is but a number")    
