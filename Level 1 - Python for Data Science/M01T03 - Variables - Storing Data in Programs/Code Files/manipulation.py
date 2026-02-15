# Request the user to input a sentence#
str_manip=input("Enter how you feel about golf?")
# Store the user input sentence as "str_manip"#
print(str_manip)
# Calculate and display the lenght of the "str_manip"#
print(len(str_manip))
# Find the last letter in "str_manip"sentence#
rep_let=(str_manip[-1])
print("The letter to be replaced with @ is "+rep_let)
# And replace every occurance of the letter with@ #
str_manip2=str_manip.replace(rep_let,"@")
# Print the original string#
print(str_manip)
#print the replaced string#
print(str_manip2)
# Print the last 3 characters in the "str_manip" backwards.#
print(str_manip[-1:-4:-1])
# Create a five-letter word that is made up of the first three characters #
# Get the first three letters in the string#
print(str_manip[0:3:1])
# Get the last two letters in the string#
print(str_manip[-2: :1])
# And the last two characters in "str_manip"#
print(str_manip[0:3:1]+str_manip[-2::1])