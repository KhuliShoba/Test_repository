import os
from tkinter import messagebox, simpledialog

class Shoe:
    """
    A class to represent a Nike shoe item in the warehouse inventory.
    Attributes:
        country (str): The country of manufacture.
        code (str): Unique product code.
        product (str): Product name or model.
        cost (float): Cost per unit.
        quantity (int): Number of units in stock.
    """
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_value(self):
        """Calculate total value: cost * quantity."""
        return self.cost * self.quantity

    def __str__(self):
        return f"{self.code}: {self.product} (Qty: {self.quantity}, Value: R{self.get_value():.2f})"

class NikeWarehouse:
    """
    Manages the Nike warehouse inventory using a list of Shoe objects.
    """
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        """Add a Shoe object to the inventory."""
        self.shoes.append(shoe)

    def search_by_code(self, code):
        """Search for a product by code and return the Shoe object."""
        for shoe in self.shoes:
            if shoe.code == code:
                return shoe
        return None

    def lowest_quantity_shoe(self):
        """Return the shoe with the lowest quantity for restocking."""
        if not self.shoes:
            return None
        return min(self.shoes, key=lambda s: s.quantity)

    def highest_quantity_shoe(self):
        """Return the shoe with the highest quantity."""
        if not self.shoes:
            return None
        return max(self.shoes, key=lambda s: s.quantity)

    def total_value_all(self):
        """Calculate total value of all stock items."""
        return sum(shoe.get_value() for shoe in self.shoes)

    def print_all_shoes(self):
        """Display all shoes in a formatted table."""
        if not self.shoes:
            print("No shoes in inventory.")
            return
        print("\n{:<12} {:<12} {:<20} {:<8} {:<8} {:<10}".format(
            "Country", "Code", "Product", "Cost", "Qty", "Value"))
        print("-" * 75)
        for shoe in self.shoes:
            print("{:<12} {:<12} {:<20} R{:<7.2f} {:<7} R{:<9.2f}".format(
                shoe.country, shoe.code, shoe.product, shoe.cost,
                shoe.quantity, shoe.get_value()))

    def update_shoe(self, code, country=None, product=None, cost=None, quantity=None):
        """Update an existing shoe's details."""
        shoe = self.search_by_code(code)
        if not shoe:
            raise ValueError("Shoe not found.")
        if country is not None:
            shoe.country = country
        if product is not None:
            shoe.product = product
        if cost is not None:
            shoe.cost = cost
        if quantity is not None:
            shoe.quantity = quantity

def clear_screen():
    """Clear the terminal screen for a clean UI."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    """Pause for user to read output."""
    input("\nPress Enter to continue...")

def main():
    warehouse = NikeWarehouse()
    # Sample data (in a real app, load from file)
    sample_shoes = [
        Shoe("ZA", "001", "Air Max 90", 1500.00, 50),
        Shoe("ZA", "002", "React Element", 2000.00, 20),
        Shoe("CN", "003", "Dunk Low", 1200.00, 75),
        Shoe("ZA", "004", "Jordan 1", 2500.00, 10)
    ]
    for shoe in sample_shoes:
        warehouse.add_shoe(shoe)

    while True:
        clear_screen()
        print("="*38)
        print("        NIKE WAREHOUSE MANAGER")
        print("="*38)
        print("1. View all shoes")
        print("2. Search by code")
        print("3. Lowest quantity (restock)")
        print("4. Highest quantity")
        print("5. Total inventory value")
        print("6. Add new shoe")
        print("7. Update shoe details")
        print("0. Exit")
        print("="*38)
        choice = input("Enter choice: ").strip()

        if choice == "1":
            clear_screen()
            warehouse.print_all_shoes()
            pause()
        elif choice == "2":
            code = input("Enter product code: ").strip()
            shoe = warehouse.search_by_code(code)
            clear_screen()
            if shoe:
                print("Product found:\n", shoe)
            else:
                print("Product not found.")
            pause()
        elif choice == "3":
            shoe = warehouse.lowest_quantity_shoe()
            clear_screen()
            if shoe:
                print(f"Restock: {shoe.product} (Code: {shoe.code}, Qty: {shoe.quantity})")
            else:
                print("No inventory.")
            pause()
        elif choice == "4":
            shoe = warehouse.highest_quantity_shoe()
            clear_screen()
            if shoe:
                print(f"Highest: {shoe.product} (Code: {shoe.code}, Qty: {shoe.quantity})")
            else:
                print("No inventory.")
            pause()
        elif choice == "5":
            total = warehouse.total_value_all()
            clear_screen()
            print(f"Total inventory value: R{total:.2f}")
            pause()
        elif choice == "6":
            clear_screen()
            print("Add New Shoe")
            country = input("Country: ").strip()
            code = input("Code: ").strip()
            product = input("Product: ").strip()
            try:
                cost = float(input("Cost: R"))
                quantity = int(input("Quantity: "))
                shoe = Shoe(country, code, product, cost, quantity)
                warehouse.add_shoe(shoe)
                print("Shoe added.")
            except ValueError:
                print("Invalid input. Cost must be a number and quantity must be an integer.")
            pause()
        elif choice == "7":
            clear_screen()
            print("Update Shoe Details")
            code = input("Enter the code of the shoe to update: ").strip()
            shoe = warehouse.search_by_code(code)
            if not shoe:
                print("Shoe not found.")
                pause()
                continue
            country = input(f"Country ({shoe.country}): ").strip() or shoe.country
            new_code = input(f"Code ({shoe.code}): ").strip() or shoe.code
            product = input(f"Product ({shoe.product}): ").strip() or shoe.product
            try:
                cost = input(f"Cost (R{shoe.cost:.2f}): ").strip()
                cost = float(cost) if cost else shoe.cost
                quantity = input(f"Quantity ({shoe.quantity}): ").strip()
                quantity = int(quantity) if quantity else shoe.quantity
                warehouse.update_shoe(code, country, new_code, product, cost, quantity)
                print("Shoe details updated.")
            except ValueError as e:
                print(f"Error updating shoe: {e}")
            pause()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            pause()

if __name__ == "__main__":
    main()
