
import math

print("FINANCIAL CALCULATOR")
print("\n" )
print("Investment - to calculate interest earned on investment")
print("Bond - to calculate monthly home loan repayments")
print("\n")

# Request the user choiceto choose and ensure it is not case sensitive
user_choice = input("Enter 'investment' or 'bond' to proceed: ").lower()

# --- INVESTMENT LOGIC ---

if user_choice == "investment":

    deposit_amount = input("Enter the deposit amount:")
    deposit_amount = deposit_amount.replace(" ","")
    p = float(deposit_amount)
    r = float(input("Enter the interest rate (as a percentage): ")) / 100
    t = int(input("Enter the number of years: "))
   
    # Selection for interest type
    interest = input("Choose 'simple' or 'compound' interest: ").lower()

    if interest == "simple":
        # Simple Interest: A = P(1 + r*t)
        A = p * (1 + r * t)
        print(f"\nSimple Interest Result: {A}")
       
    elif interest == "compound":
        # Compound Interest: A = P(1 + r)^t
        A = p * math.pow((1 + r), t)
        print(f"\nCompound Interest Result: {A}")
   
    else:
        print("Error: Invalid interest type selected.")

# --- BOND LOGIC ---
elif user_choice == "bond":
    value_House = input("Enter the current value of the house: ")

    value_House =value_House.replace(" ","")
    p= float(value_House)
   
    annual_rate = float(input("Enter the annual interest rate: "))
    # Convert annual rate to a monthly decimal
    i = (annual_rate / 100) / 12
    n = int(input("Enter the number of months for repayment: "))

    # Bond Repayment Formula: x = (i * P) / (1 - (1 + i)^-n)
    repayment = (i * p) / (1 - math.pow((1 + i), -n))
    print(f"\nMonthly Bond Repayment: {repayment}")
     
else:
    print("Error: Invalid selection. Please enter 'investment' or 'bond'.")
