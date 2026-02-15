class Shoe:
    # The Shoe class represents a shoe in the inventory with attributes for country, code, product name, cost, and quantity.
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
        # Table-formatted string with proper alignment
        return f"{self.country:<15} {self.code:<10} {self.product:<20} {self.cost:<10.2f} {self.quantity:<10}"

# The NikeWarehouse class manages a collection of Shoe objects, allowing for operations like adding shoes, searching by code, and calculating inventory values.
shoe_list = []

def read_shoes_data():
    try:    
        with open('inventory.txt', 'r', encoding='utf-8') as file:
            next(file)  # Skip the first line
            for line in file:
                data = line.strip().split(',')
                if len(data) != 5:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                try:
                    shoe = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
                    shoe_list.append(shoe)
                except ValueError:
                    print(f"Skipping line with invalid  {line.strip()}")
    except FileNotFoundError:
        print("The file inventory.txt was not found.")
    except StopIteration:
        print("The file is empty or has no data lines.")
    except Exception as e:
        print(f"An error occurred: {e}")                

# Menu functions
def capture_shoes():
    while True:
        try:
            country = input("Enter the Country: ")
            code = input("Enter the Code: ")
            product = input("Enter the Product: ")
            cost = float(input("Enter the Cost: "))
            quantity = int(input("Enter the Quantity: "))
            
            if cost < 0 or quantity < 0:
                print("Cost and quantity must be non-negative. Please try again.")
                continue
                
            shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(shoe)
            print("Shoe added successfully!")
            break
            
        except ValueError:
            print("Invalid input for cost or quantity. Please enter numeric values.")

def view_all():
    if not shoe_list:
        print("No shoes in inventory.")
        return
    
    # Print header
    header = f"{'No.':<5} {'Country':<15} {'Code':<10} {'Product':<20} {'Cost':<10} {'Quantity':<10}"
    print(header)
    print('-' * len(header))
    
    # Iterate and print using __str__ method
    for idx, shoe in enumerate(shoe_list, start=1):
        print(f"{idx:<5} {shoe}")

def save_shoes_data():
    try:
        with open('inventory.txt', 'w') as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        print("Data saved to inventory.txt.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def re_stock():
    if not shoe_list:
        print("No shoes in inventory.")
        return
    
    # Find the shoe with the lowest quantity
    min_shoe = min(shoe_list, key=lambda s: s.quantity)
    print("\nShoe with the lowest quantity:")
    print(f"Country: {min_shoe.country}, Code: {min_shoe.code}, Product: {min_shoe.product}, Cost: {min_shoe.cost}, Quantity: {min_shoe.quantity}")
    try:
        add_qty = int(input(f"Do you want to add stock to this shoe? Enter quantity to add (0 to skip): "))
        if add_qty > 0:
            min_shoe.quantity += add_qty
            save_shoes_data()
            print(f"Updated quantity for {min_shoe.product} (Code: {min_shoe.code}): {min_shoe.quantity}")
        else:
            print("No stock added.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def search_shoe():
    if not shoe_list:
        print("No shoes in inventory.")
        return
    code = input("Enter the shoe code to search: ").strip()
    found = False
    for shoe in shoe_list:
        if shoe.code.lower() == code.lower():
            print("\nShoe found:")
            print(f"Country: {shoe.country}, Code: {shoe.code}, Product: {shoe.product}, Cost: {shoe.cost}, Quantity: {shoe.quantity}")
            found = True
            break
    if not found:
        print("No shoe found with that code.")

def value_per_item():
    if not shoe_list:
        print("No shoes in inventory.")
        return
    header = f"{'No.':<5} {'Country':<15} {'Code':<10} {'Product':<20} {'Cost':<10} {'Quantity':<10} {'Value':<12}"
    print(header)
    print('-' * len(header))
    for idx, shoe in enumerate(shoe_list, start=1):
        value = shoe.cost * shoe.quantity
        print(f"{idx:<5} {shoe.country:<15} {shoe.code:<10} {shoe.product:<20} {shoe.cost:<10.2f} {shoe.quantity:<10} {value:<12.2f}")

def highest_qty():
    if not shoe_list:
        print("No shoes in inventory.")
        return
    max_shoe = max(shoe_list, key=lambda s: s.quantity)
    print("\nShoe with the highest quantity (FOR SALE!):")
    print(f"Country: {max_shoe.country}, Code: {max_shoe.code}, Product: {max_shoe.product}, Cost: {max_shoe.cost}, Quantity: {max_shoe.quantity}")

def total_inventory_value():
    if not shoe_list:
        print("No shoes in inventory.")
        return
    total_value = sum(shoe.cost * shoe.quantity for shoe in shoe_list)
    print(f"\nTotal inventory value: ${total_value:.2f}")

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
        if choice == '1':
            view_all()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            save_shoes_data()
        elif choice == '4':
            re_stock()
        elif choice == '5':
            search_shoe()
        elif choice == '6':
            value_per_item()
        elif choice == '7':
            highest_qty()
        elif choice == '8':
            total_inventory_value()
        elif choice == '9':
            print("Thank you for using the Shoe Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    main()

