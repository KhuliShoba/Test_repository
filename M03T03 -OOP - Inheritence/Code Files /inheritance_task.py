class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Class attribute for the head office location
    head_office = "Cape Town"
   
    def __init__(self):
        self.name = "Fundamentals of Computer Science"
        self.contact_website = "www.hyperiondev.com"
        self.head_office = "Cape Town"

    # Method to display contact details
    def contact_details(self):
        print("Course Name:", self.name)
        print("Please contact us by visiting", self.contact_website)
        print("Head Office location:", self.head_office)

# Create an instance and call methods
class OOPCourse(Course):
    def __init__(self):
        super().__init__()
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mous"
        self.course_ID = "12345"  
    

    def trainer_details(self):
        print("Trainer Name:", self.trainer)    
        print("Course Description:", self.description)
    def show_course_ID(self):
        print("Course ID:", self.course_ID)

# Create an instance and call methods
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_ID()

