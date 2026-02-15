# Determine an award a person competing in a triathlon will receive.

# Request a user input for the minutes it took into complete swimming triathlon 
swimming_minutes=int(input(" Enter how many minutes it took to complete your swimming triathlon? "))
# Request a user input for the minutes it took into complete cycling triathlon 
cycling_minutes=int(input(" Enter how many minutes it took to complete your cycling triathlon? "))
# Request a user input for the minutes it took into complete running triathlon 
running_minutes=int(input(" Enter how many minutes it took to complete your running triathlon? "))
# Print all minutes inputs
print(swimming_minutes)
print(cycling_minutes)
print(running_minutes)
# Calculate the total minutes to complete the triathlon
sum=(swimming_minutes+cycling_minutes+running_minutes)
# Print the sum of thriathlon minutes
print("Total time taken for the triathlon:",sum, "minutes")
# Classify the award the user receive based on the total minutes
if sum <= 100: 
    print("Award: Provincial Colours.")

elif sum <= 105: 
    print(" Award: Provincial half colours") 

elif sum <= 110:
    print(" Award: Provincial scroll")  
       
else: 
    print("No Award")








