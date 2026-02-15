class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost    

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        # Table formatting moved inside __str__ as requested
        # Use fixed widths to ensure columns align when printed in a list
        return f"{self.country:<15} {self.code:<10} {self.product:<20} {self.cost:<10.2f} {self.quantity:<10}"

shoe_list = []

def read_shoes_data():
    try:    
        with open('inventory.txt', 'r', encoding='utf-8') as file:
            next(file)  # Skip the header
            for line in file:
                data = line.strip().split(',')
                if len(data) != 5:
                    continue
                try:
                    shoe = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
                    shoe_list.append(shoe)
                except ValueError:
                    print(f"Skipping line with invalid data: {line.strip()}")
    except FileNotFoundError:
        print("The file inventory.txt was not found.")

def capture_shoes():
    country = input("Enter the Country: ")
    code = input("Enter the Code: ")
    product = input("Enter the Product: ")
    
    # Loop for Cost validation
    while True:
        try:
            cost = float(input("Enter the Cost: "))
            if cost < 0:
                print("Cost cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for cost.")

    # Loop for Quantity validation
    while True:
        try:
            quantity = int(input("Enter the Quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")

    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    print("Shoe added successfully!")

def view_all():
    if not shoe_list:
        print("No shoes in inventory.")
        return
    
    header = f"{'No.':<5} {'Country':<15} {'Code':<10} {'Product':<20} {'Cost':<10} {'Quantity':<10}"
    print("\n" + header)
    print('-' * len(header))
    
    # Now iterating and printing the shoe object directly calls __str__
    for idx, shoe in enumerate(shoe_list, start=1):
        print(f"{idx:<5} {shoe}")

def save_shoes_data():
    try:
        with open('inventory.txt', 'w') as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                # We don't use __str__ here because the file needs CSV format, not table format
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        print("Data saved to inventory.txt.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def re_stock():
    if not shoe_list:
        print("No shoes in inventory.")
        return
    min_shoe = min(shoe_list, key=lambda s: s.quantity)
    print(f"\nLowest stock: {min_shoe.product} ({min_shoe.quantity} units left)")
    
    while True:
        try:
            add_qty = int(input(f"Enter quantity to add to {min_shoe.product}: "))
            if add_qty < 0:
                print("Please enter a positive number.")
                continue
            min_shoe.quantity += add_qty
            save_shoes_data()
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

def search_shoe():
    code = input("Enter the shoe code to search: ").strip()
    for shoe in shoe_list:
        if shoe.code.lower() == code.lower():
            print(f"\n{'Country':<15} {'Code':<10} {'Product':<20} {'Cost':<10} {'Quantity':<10}")
            print(shoe)
            return
    print("No shoe found with that code.")

def value_per_item():
    header = f"{'Product':<20} {'Total Value':<12}"
    print("\n" + header)
    print("-" * len(header))
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product:<20} ${value:<12.2f}")

def highest_qty():
    if not shoe_list: return
    max_shoe = max(shoe_list, key=lambda s: s.quantity)
    print(f"\nFOR SALE: {max_shoe.product} has the highest quantity ({max_shoe.quantity})")

def total_inventory_value():
    total = sum(shoe.cost * shoe.quantity for shoe in shoe_list)
    print(f"\nTotal Stock Value: ${total:,.2f}")

def main():
    read_shoes_data()
    menu = """
========= Shoe Inventory Menu =========
1. View all shoes
2. Add new shoe
3. Save data
4. Restock lowest quantity
5. Search shoe by code
6. Show value per item
7. Show highest quantity (FOR SALE)
8. Show total inventory value
9. Exit
=======================================
"""
    while True:
        print(menu)
        choice = input("Select an option (1-9): ").strip()
        if choice == '1': view_all()
        elif choice == '2': capture_shoes()
        elif choice == '3': save_shoes_data()
        elif choice == '4': re_stock()
        elif choice == '5': search_shoe()
        elif choice == '6': value_per_item()
        elif choice == '7': highest_qty()
        elif choice == '8': total_inventory_value()
        elif choice == '9': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()