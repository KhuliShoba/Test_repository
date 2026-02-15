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
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


shoe_list = []
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
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
                    print(f"Skipping line with invalid data: {line.strip()}")
    except FileNotFoundError:
        print("The file inventory.txt was not found.")
    except StopIteration:
        print("The file is empty or has no data lines.")
    except Exception as e:
        print(f"An error occurred: {e}")                


def capture_shoes():
    try:
        country = input("Enter the country: ")
        code = input("Enter the code: ")
        product = input("Enter the product: ")
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))
        if cost < 0 or quantity < 0:
            print("Cost and quantity must be non-negative.")
            return
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
    except ValueError:
        print("Invalid input for cost or quantity. Please enter numeric values.")

def view_all():
    for shoe in shoe_list:
        print(shoe)

def save_shoes_data():
    try:
        with open('inventory.txt', 'w') as file:
            file.write("Country,Code,Product,Cost,Quantity\n")  # Header
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
        print("Data saved to inventory.txt.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

