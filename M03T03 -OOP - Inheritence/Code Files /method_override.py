# Define a class called Adult with attributes name, age, hair_colour, and eye_colour method called can drive

class Adult: 
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour
        self.can_drive = self.age >= 18

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Hair Colour: {self.hair_colour}")
        print(f"Eye Colour: {self.eye_colour}")
        print(f"Can Drive: {self.can_drive}")

# Request user input for the attributes
input_name = input("Enter your name: ")
input_age = int(input("Enter your age: "))
input_hair_colour = input("Enter your hair colour: ")
input_eye_colour = input("Enter your eye colour: ")

# Create an instance of the Adult class with user input   
adult = Adult(input_name, input_age, input_hair_colour, input_eye_colour)
adult.display_info()

# Define a Child class that inherits from the Adult class same attributes and overides can drive method.
class Child(Adult):
    def __init__(self, name, age, hair_colour, eye_colour):
        super().__init__(name, age, hair_colour, eye_colour)

    def can_drive(self):
        if self.age >= 18:
            print(f"{self.name} old enough to drive.")
        else:
            print(f"{self.name} too young to drive.")

child = Child(input_name, input_age, input_hair_colour, input_eye_colour)

if child.age < 18:
    print(f"{child.name} is too young to drive.")
else:
    print(f"{child.name} can drive.")
