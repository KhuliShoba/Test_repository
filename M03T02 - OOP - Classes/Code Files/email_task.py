"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    def __init__(self, email_address, subject_line, email_content):
        # Initialise the instance variables for each email. 
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

# Provide a string representation of the Email object.
    def __str__(self) -> str:
        return f"From: {self.email_address}\nSubject: {self.subject_line}\n\n{self.email_content}"

    # Create the 'mark_as_read()' method to change the 'has_been_read'
    # instance variable for a specific object from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Functions --- #
# Build out the required functions for your program.
inbox = []

def populate_inbox():
    # Create 3 sample emails and add them to the inbox list.
    email1 = Email(
        "support@hyperiondev.com",
        "Welcome to HyperionDev!",
        "Welcome to HyperionDev! I trust you will enjoy your studies here.."
    )
    email2 = Email(
        "teacher@hyperiondev.com",
        "Great work on the bootcamp!",
        "Keep up the excellent progress you're making."
    )
    email3 = Email(
        "admin@hyperiondev.com",
        "Your excellent marks!",
        "Congratulations on your outstanding test scores!"
    )
      
    inbox.extend([email1, email2, email3])  


def list_emails():
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    print("Inbox:")
    for index, email in enumerate(inbox):
        status = "Read" if email.has_been_read else "Unread"
        print(f"{index}. {email.subject_line} - {status}")
    
def read_email(index):
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
        print(f"\nEmail from {email.email_address} marked as read.")
    else:
        print("Invalid email index.Please try again.")

def view_unread_emails():
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    unread_emails = [email for email in inbox if not email.has_been_read]
    if unread_emails:
        print("\nUnread Emails:")
        for index, email in enumerate(unread_emails):
            original_index = inbox.index(email) 
            print(f"{original_index}. {email.subject_line}")

    else:
        print("\nNo unread emails.")

# --- Lists --- #
# --- Email Program --- #
# Initial population of the inbox for further use in your program.
populate_inbox()    

while True:
    try:
        user_input = int(
            input(
                """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """))

        if user_input == 1:
            # List all emails so the user knows which index to choose
            list_emails()
            try:
                index = int(input("Enter the index of the email you want to read: "))
                read_email(index)
            except ValueError:  
                print("Invalid input. Please enter a number.")

        elif user_input == 2:
            # Retrieve only the subject lines of unread emails
            view_unread_emails()    
            
        elif user_input == 3:
            # Add logic here to quit application.
            print("Exiting the email application. Goodbye!")
            break       
        
        else:
            print("Invalid input. Please enter a number.")
    except ValueError:
        print("Invalid input. Please enter a number.")    