# Request the user to input a number between 1 and 100
num = int(input("Please input a number between 1 and 100: "))

# Check if the number is lower than 12, higher than 13 or exactly 13.
if num < 12: 
    print(" The value you entered is lower than 12")
elif num > 13:
    print("The value you entered is higher than 13")
elif num < 13:
    print("The value you entered is lower than 13")
else:
    print("The value you entered is 13")


    # Request the user to input a number between 10 and 1000
num = int(input("Please input a number between 10 and 1000: "))

# Check if the number is lower than 50, higher than 52 or exactly 52.
if num < 50: 
    print(" The value you entered is lower than 50")
elif num > 52:
    print("The value you entered is higher than 52")
elif num < 52:
    print("The value you entered is lower than 52")
else:
    print("The value you entered is 52")


# Checks the current time and suggest an activity#
current_time = 12
if current_time < 11:
    print("Time for a short jog - let's go!")
else:
    print("It's after 11 - it's lunch time.")    

 # Checks the current time and suggest an activity#
current_time = 11
if current_time == 11:
    print("Time for a short jog - let's go!")
else:
    print("It's after 11 - it's lunch time.")  

# Check the current hour and sets a greeting based on the time of the day#
# Request the user to input the current hour#
current_hour=int(input("Enter your current hour:")) 
# Store the user input as "current_hour"           
if current_hour < 18: 
   print("Good day")
elif current_hour <20:
    print("Good evening")
else:
   print("Good night")