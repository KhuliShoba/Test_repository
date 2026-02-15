def plane_cost(city):
    x = 0
    if city == "Cape Town":
        x = 2091
    elif city == "Durban":
        x = 1788
    elif city == "Port Elizabeth":
        x = 1277
    elif city == "George":
        x = 1975
    y = x
    return y

def hotel_cost(nights):
    a = 0
    if nights == 1:
        a = 500
    elif nights == 2:
        a = 1000
    elif nights == 3:
        a = 1500
    elif nights == 4:
        a = 2000
    elif nights == 5:
        a = 2500
    elif nights == 6:
        a = 3000
    elif nights == 7:
        a = 3500
    b = a
    return b

def car_rental(days):            
    m = 0  
    if days == 1:
        a = 200
    elif days == 2:
        a = 400
    elif days == 3:
        a = 600
    elif days == 4:
        a = 800 
    elif days == 5:
        a = 1000
    elif days == 6:
        a = 1200 
    elif days == 7:
        a = 1400   
        m = a
    return m

def holiday_cost(city,nights,days):
    total = plane_cost(city) + hotel_cost(nights) + car_rental(days)
    return total
city = input("Enter the city you want to visit: Cape Town, Durban, Port Elizabeth, George: ")
nights=int(input("Enter the number of nights you will stay at the hotel: 1-7: "))
days = int(input("Enter the number of days you will rent the car: 1-7 "))

total_cost = holiday_cost(city,nights,days)
print(f"The total cost of your holiday to {city} for {nights} nights, and {days} days of car rental is: R {total_cost}")