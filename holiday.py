# --- Holiday Cost Calculator ---

def plane_cost(city):
    # Simply return the cost based on the city
    if city == "Cape Town":
        return 2091
    elif city == "Durban":
        return 1788
    elif city == "Port Elizabeth":
        return 1277
    elif city == "George":
        return 1975
    else:
        return 0

def hotel_cost(nights):
    # Multiply nights by the nightly rate (R500)
    return nights * 500

def car_rental(days):            
    # Multiply days by the daily rate (R200)
    return days * 200

def holiday_cost(city, nights, days):
    # Summing the results of the functions
    total = plane_cost(city) + hotel_cost(nights) + car_rental(days)
    return total

# --- Main Program ---
# Get user input for city, nights, and days
city = input("Enter the city (Cape Town, Durban, Port Elizabeth, George): ").title().strip()
nights = int(input("Enter the number of nights you will stay: "))
days = int(input("Enter the number of days you will rent the car: "))

# Calculate total holiday cost
total_cost = holiday_cost(city, nights, days)

print("\n" + "-"*30)
print(f"Destination: {city}")
print(f"Total Holiday Cost: R{total_cost:,.2f}")
print("-"*30)
