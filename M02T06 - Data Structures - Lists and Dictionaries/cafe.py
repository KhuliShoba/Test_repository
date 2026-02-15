menu_list = [ "Coffee", "Sandwich", "Burger", "Coke", "Chips"]

# Create a stock disctionary with stock values for each stock item
stock = {"Coffee":10 ,
         "Sandwich":20,
         "Burger":15,
         "Coke" :50,
         "Chips":40
}
stock_dict = dict(stock)   

# Create a price list dictionary with prices for each item on the menu (in Rands)
price = {"Coffee": 8.00,
        "Sandwich":15.00,
        "Burger": 20.00,
        "Coke": 10.00,
        "Chips": 12.00
}
# Calculate total worth of stock by looping through menu items
total_stock = 0
for item in menu_list:

    # Multiply stock quantity by price for each item
    item_value = stock[item] * price[item]
    total_stock += item_value

   
print("------- Cafe Stock Report ------")
print(f"Menu: {menu_list}")
print(f"Stock: {stock}")
print(f"Prices: {price}")
print(f"Total stock worth: R{total_stock}")

            
