# ===== Importing external modules ===========
from datetime import datetime
import re

# ===== User Class =====

class User:
    """
    Represents a user in the Task Manager system.
    Attributes:
        username (str): The user's unique username (3-20 alphanumeric + underscores)
        password (str): The user's password (minimum 6 characters)
        role (str): The user's role ('Admin' or 'Non-Admin')
    """
    
    def __init__(self, username, password, role):
        """
        Initialize a User object with username, password, and role.
        
        Args:
            username (str): The user's username
            password (str): The user's password
            role (str): The user's role ('Admin' or 'Non-Admin')
        """
        self.username = username
        self.password = password
        self.role = role
    
    def __str__(self):
        """
        Return string representation of the user.
        Format: username, password, role
        """
        return f"{self.username}, {self.password}, {self.role}"
    
    def display_info(self):
        """
        Display user information in formatted tabular output.
        """
        print(f"  {'Username':<30} | {self.username}")
        print(f"  {'Role':<30} | {self.role}")
        print("  " + "-" * 76)


# ===== Validation Functions =====

def validate_username(username):
    """
    Validate username format.
    Username must be 3-20 characters and contain only alphanumeric characters and underscores.
    Returns: (is_valid, error_message)
    """
    if not username:
        return False, "Username cannot be empty."
    if len(username) < 3:
        return False, "Username must be at least 3 characters long."
    if len(username) > 20:
        return False, "Username must be no more than 20 characters long."
    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        return False, "Username can only contain letters, numbers, and underscores."
    return True, ""


def validate_password(password):
    """
    Validate password strength.
    Password must be at least 6 characters long.
    Returns: (is_valid, error_message)
    """
    if not password:
        return False, "Password cannot be empty."
    if len(password) < 6:
        return False, "Password must be at least 6 characters long."
    return True, ""


def validate_date_format(date_string):
    """
    Validate date format (YYYY-MM-DD).
    Returns: (is_valid, error_message)
    """
    if not date_string:
        return False, "Date cannot be empty."
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Invalid date format. Please use YYYY-MM-DD."


def validate_non_empty(input_string, field_name):
    """
    Validate that input is not empty.
    Returns: (is_valid, error_message)
    """
    if not input_string or not input_string.strip():
        return False, f"{field_name} cannot be empty."
    return True, ""


def validate_role(role):
    """
    Validate that role is either 'Admin' or 'Non-Admin'.
    Returns: (is_valid, error_message)
    """
    valid_roles = ['admin', 'non-admin']
    if role.lower() not in valid_roles:
        return False, "Role must be either 'Admin' or 'Non-Admin'."
    return True, ""


def login_user():
    """
    Authenticate a user by username and password.
    Returns: User object if authentication successful, None otherwise.
    """
    print_header("USER LOGIN")
    
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ")
    
    try:
        with open("user.txt", "r") as user_file:
            for line in user_file:
                user_data = line.strip().split(", ")
                if len(user_data) == 3:
                    file_username, file_password, role = user_data
                    if file_username == username and file_password == password:
                        user = User(file_username, file_password, role)
                        print_header("SUCCESS")
                        print(f"  Welcome, {user.username}!")
                        print(f"  Role: {user.role}")
                        print()
                        return user
        
        # Authentication failed
        print_header("ERROR")
        print("  Invalid username or password. Please try again.")
        print()
        return None
    except FileNotFoundError:
        print_header("ERROR")
        print("  No users found. Please register first.")
        print()
        return None
    except IOError as e:
        print_header("ERROR")
        print(f"  Error during login: {e}")
        print()
        return None


# ===== Function Definitions =====

def print_header(title):
    """
    Print a formatted header for sections.
    """
    print("\n" + "=" * 80)
    print(f"  {title.center(76)}")
    print("=" * 80)


def verify_and_update_user_roles():
    """
    Check all existing users in user.txt for missing roles.
    For users without roles (old format: username, password),
    prompt to assign them a role and update the file.
    """
    try:
        with open("user.txt", "r") as user_file:
            lines = user_file.readlines()
        
        needs_update = False
        updated_lines = []
        
        print_header("USER ROLE VERIFICATION")
        
        for line in lines:
            user_data = line.strip().split(", ")
            
            # Check if user has a role (3 fields) or not (2 fields)
            if len(user_data) == 2:
                # Old format: username, password (no role)
                username, password = user_data
                needs_update = True
                
                print(f"\n  User '{username}' found without a role assignment.")
                
                # Ask user to assign role
                while True:
                    print(f"  Assign role for '{username}':")
                    print("    1 - Admin")
                    print("    2 - Non-Admin")
                    role_choice = input("  Enter your choice (1 or 2): ").strip()
                    
                    if role_choice == "1":
                        role = "Admin"
                        break
                    elif role_choice == "2":
                        role = "Non-Admin"
                        break
                    else:
                        print("  Error: Invalid choice. Please enter 1 or 2.")
                
                # Create updated user entry with role
                updated_user = User(username, password, role)
                updated_lines.append(str(updated_user) + "\n")
                print(f"  ✓ Role '{role}' assigned to '{username}'.")
                
            elif len(user_data) == 3:
                # New format: username, password, role (already has role)
                updated_lines.append(line)
        
        # If updates were made, save the updated file
        if needs_update:
            with open("user.txt", "w") as user_file:
                user_file.writelines(updated_lines)
            print_header("SUCCESS")
            print("  All users have been updated with roles!")
            print()
        else:
            if lines:
                print("  All existing users already have roles assigned.")
                print()
    
    except FileNotFoundError:
        # No user.txt file exists yet, which is fine
        pass
    except IOError as e:
        print_header("ERROR")
        print(f"  Error updating user roles: {e}")
        print()


def register_user():
    """
    Register a new user by collecting username, password, and role.
    Creates a User object and saves it to user.txt.
    Validates username format, password strength, and role selection.
    Checks for duplicate usernames before saving.
    """
    # Get and validate username
    while True:
        username = input("Enter a username: ").strip()
        is_valid, error_msg = validate_username(username)
        if not is_valid:
            print(f"Error: {error_msg}")
            continue
        # Check if username already exists
        username_exists = False
        try:
            with open("user.txt", "r") as user_file:
                for line in user_file:
                    existing_user = line.strip().split(", ")[0]
                    if existing_user == username:
                        username_exists = True
                        break
        except FileNotFoundError:
            pass  # File doesn't exist yet, so username is unique
        if username_exists:
            print(f"Error: Username '{username}' already exists. Please try a different username.")
            continue
        else:
            break  # Username is unique, proceed
    
    # Get and validate password
    while True:
        password = input("Enter a password: ")
        is_valid, error_msg = validate_password(password)
        if not is_valid:
            print(f"Error: {error_msg}")
            continue
        break
    
    # Get and validate password confirmation
    while True:
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            break
        else:
            print("Error: Passwords do not match. Please try again.")
    
    # Get and validate role
    while True:
        print("\n  Select user role:")
        print("    1 - Admin")
        print("    2 - Non-Admin")
        role_choice = input("  Enter your choice (1 or 2): ").strip()
        
        if role_choice == "1":
            role = "Admin"
            break
        elif role_choice == "2":
            role = "Non-Admin"
            break
        else:
            print("Error: Invalid choice. Please enter 1 or 2.")
    
    # Create User object
    new_user = User(username, password, role)
    
    # Save user to file
    try:
        with open("user.txt", "a") as user_file:
            user_file.write(str(new_user) + "\n")
        print_header("SUCCESS")
        print(f"  User '{new_user.username}' successfully created!")
        print(f"  Role: {new_user.role}")
        print()
    except IOError as e:
        print_header("ERROR")
        print(f"  Error saving user: {e}")
        print()


def add_task():
    """
    Create a new task and assign it to a user.
    Validates all inputs before saving to task.txt.
    Format: username, title, description, due_date, assigned_date, complete
    """
    # Validate task username
    while True:
        task_username = input("Enter the username to assign the task to: ").strip()
        is_valid, error_msg = validate_non_empty(task_username, "Username")
        if not is_valid:
            print(f"Error: {error_msg}")
            continue
        break
    
    # Validate task title
    while True:
        task_title = input("Enter the task title: ").strip()
        is_valid, error_msg = validate_non_empty(task_title, "Task title")
        if not is_valid:
            print(f"Error: {error_msg}")
            continue
        break
    
    # Validate task description
    while True:
        task_description = input("Enter the task description: ").strip()
        is_valid, error_msg = validate_non_empty(task_description, "Task description")
        if not is_valid:
            print(f"Error: {error_msg}")
            continue
        break
    
    # Validate due date
    while True:
        task_due_date = input("Enter the due date (YYYY-MM-DD): ").strip()
        is_valid, error_msg = validate_date_format(task_due_date)
        if not is_valid:
            print(f"Error: {error_msg}")
            continue
        break
    
    # Get current date and set task as not complete
    current_date = datetime.now().strftime("%Y-%m-%d")
    task_complete = "No"
    
    # Save task to file
    try:
        with open("task.txt", "a") as task_file:
            task_file.write(f"{task_username}, {task_title}, {task_description}, {task_due_date}, {current_date}, {task_complete}\n")
        print_header("SUCCESS")
        print(f"  Task '{task_title}' successfully added!")
        print(f"  Assigned to: {task_username}")
        print()
    except IOError as e:
        print_header("ERROR")
        print(f"  Error saving task: {e}")
        print()


def display_task(username, title, description, due_date, assigned_date, complete):
    """
    Display a single task in formatted tabular output.
    Helper function to reduce code duplication.
    """
    print(f"  {'Username':<20} | {username}")
    print(f"  {'Task Title':<20} | {title}")
    print(f"  {'Description':<20} | {description}")
    print(f"  {'Due Date':<20} | {due_date}")
    print(f"  {'Assigned Date':<20} | {assigned_date}")
    print(f"  {'Status':<20} | {complete}")
    print("  " + "-" * 76)


def display_task_for_user(username, title, description, due_date, assigned_date, complete):
    """
    Display a task for the user's own view (excludes username field).
    Helper function for view_my_tasks() in formatted tabular output.
    """
    print(f"  {'Task Title':<20} | {title}")
    print(f"  {'Description':<20} | {description}")
    print(f"  {'Due Date':<20} | {due_date}")
    print(f"  {'Assigned Date':<20} | {assigned_date}")
    print(f"  {'Status':<20} | {complete}")
    print("  " + "-" * 76)


def view_all_tasks():
    """
    Read and display all tasks from task.txt in formatted tabular manner.
    Parses each line and validates it has all 6 required fields.
    Handles file I/O errors gracefully.
    """
    try:
        with open("task.txt", "r") as task_file:
            tasks = []
            for line in task_file:
                task_data = line.strip().split(", ")
                if len(task_data) == 6:
                    tasks.append(task_data)
            
            if len(tasks) == 0:
                print_header("ALL TASKS")
                print("  No tasks found.")
                print()
            else:
                print_header("ALL TASKS")
                for username, title, description, due_date, assigned_date, complete in tasks:
                    display_task(username, title, description, due_date, assigned_date, complete)
                print(f"  Total tasks: {len(tasks)}")
                print()
    except FileNotFoundError:
        print_header("ALL TASKS")
        print("  No tasks found.")
        print()
    except IOError as e:
        print_header("ERROR")
        print(f"  Error reading tasks: {e}")
        print()


def view_all_users():
    """
    Read and display all registered users from user.txt in formatted tabular manner.
    Creates User objects from file data and displays them.
    Handles file I/O errors gracefully.
    """
    try:
        with open("user.txt", "r") as user_file:
            users = []
            for line in user_file:
                user_data = line.strip().split(", ")
                if len(user_data) == 3:
                    username, password, role = user_data
                    user = User(username, password, role)
                    users.append(user)
            
            if len(users) == 0:
                print_header("ALL USERS")
                print("  No users found.")
                print()
            else:
                print_header("ALL USERS")
                for user in users:
                    user.display_info()
                print(f"  Total users: {len(users)}")
                print()
    except FileNotFoundError:
        print_header("ALL USERS")
        print("  No users found.")
        print()
    except IOError as e:
        print_header("ERROR")
        print(f"  Error reading users: {e}")
        print()


def view_my_tasks():
    """
    Display only tasks assigned to the specified user.
    Validates username input before querying tasks in tabular format.
    """
    while True:
        my_username = input("Enter your username: ").strip()
        is_valid, error_msg = validate_non_empty(my_username, "Username")
        if not is_valid:
            print(f"Error: {error_msg}")
            continue
        break
    
    try:
        with open("task.txt", "r") as task_file:
            user_tasks = []
            
            for line in task_file:
                task_data = line.strip().split(", ")
                
                if len(task_data) == 6:
                    username, title, description, due_date, assigned_date, complete = task_data
                    
                    if username == my_username:
                        user_tasks.append((username, title, description, due_date, assigned_date, complete))
            
            print_header(f"MY TASKS - {my_username.upper()}")
            
            if len(user_tasks) == 0:
                print(f"  No tasks found for user '{my_username}'.")
            else:
                for username, title, description, due_date, assigned_date, complete in user_tasks:
                    display_task_for_user(username, title, description, due_date, assigned_date, complete)
                print(f"  Total tasks assigned to you: {len(user_tasks)}")
            print()
    except FileNotFoundError:
        print_header(f"MY TASKS - {my_username.upper()}")
        print("  No tasks found.")
        print()
    except IOError as e:
        print_header("ERROR")
        print(f"  Error reading tasks: {e}")
        print()


def display_menu():
    """
    Display the main menu with formatted header and return the user's choice.
    """
    print_header("MAIN MENU")
    menu = input(
        '''  r - Register a user
  a - Add task
  va - View all tasks
  vm - View my tasks
  vu - View all users
  vr - Verify and update user roles
  e - Exit

  Enter your choice: '''
    ).lower()
    return menu


def display_admin_menu():
    """
    Display the admin-only menu with formatted header and return the user's choice.
    Admin has access to all features.
    """
    print_header(f"ADMIN MENU")
    menu = input(
        '''  r - Register a user (Admin only)
  a - Add task
  va - View all tasks
  vm - View my tasks
  vu - View all users (Admin only)
  vr - Verify and update user roles (Admin only)
  dt - Delete task (Admin only)
  vc - View completed tasks (Admin only)
  lo - Logout
  e - Exit

  Enter your choice: '''
    ).lower()
    return menu


def display_non_admin_menu():
    """
    Display the non-admin-only menu with formatted header and return the user's choice.
    Non-Admin has limited access.
    """
    print_header(f"USER MENU")
    menu = input(
        '''  a - Add task
  va - View all tasks
  vm - View my tasks
  lo - Logout
  e - Exit

  Enter your choice: '''
    ).lower()
    return menu


def delete_task():
    """
    Delete a task from task.txt (Admin only).
    Prompts for task details to identify and delete the task.
    """
    print_header("DELETE TASK")
    
    task_title = input("Enter the task title to delete: ").strip()
    
    try:
        with open("task.txt", "r") as task_file:
            lines = task_file.readlines()
        
        found = False
        updated_lines = []
        
        for line in lines:
            task_data = line.strip().split(", ")
            if len(task_data) == 6:
                username, title, description, due_date, assigned_date, complete = task_data
                if title == task_title:
                    found = True
                    print_header("SUCCESS")
                    print(f"  Task '{task_title}' has been deleted.")
                    print()
                    continue
            updated_lines.append(line)
        
        if found:
            with open("task.txt", "w") as task_file:
                task_file.writelines(updated_lines)
        else:
            print_header("ERROR")
            print(f"  Task '{task_title}' not found.")
            print()
    except FileNotFoundError:
        print_header("ERROR")
        print("  No tasks found.")
        print()
    except IOError as e:
        print_header("ERROR")
        print(f"  Error deleting task: {e}")
        print()


def view_completed_tasks():
    """
    View all completed tasks (Admin only).
    Displays tasks with 'Yes' completion status.
    """
    try:
        with open("task.txt", "r") as task_file:
            completed_tasks = []
            for line in task_file:
                task_data = line.strip().split(", ")
                if len(task_data) == 6:
                    username, title, description, due_date, assigned_date, complete = task_data
                    if complete.lower() == "yes":
                        completed_tasks.append(task_data)
            
            print_header("COMPLETED TASKS")
            
            if len(completed_tasks) == 0:
                print("  No completed tasks found.")
            else:
                for username, title, description, due_date, assigned_date, complete in completed_tasks:
                    display_task(username, title, description, due_date, assigned_date, complete)
                print(f"  Total completed tasks: {len(completed_tasks)}")
            print()
    except FileNotFoundError:
        print_header("COMPLETED TASKS")
        print("  No tasks found.")
        print()
    except IOError as e:
        print_header("ERROR")
        print(f"  Error reading tasks: {e}")
        print()


def main():
    """
    Main program loop with role-based access control.
    Admin users have full access to all features.
    Non-Admin users have limited access (add task, view my tasks only).
    """
    print_header("WELCOME TO TASK MANAGER")
    
    # Verify and update existing users with roles on startup
    verify_and_update_user_roles()
    
    while True:
        # Login loop
        while True:
            current_user = login_user()
            if current_user:
                break
        
        # User session loop
        user_logged_in = True
        while user_logged_in:
            # Display menu based on user role
            if current_user.role.lower() == "admin":
                menu = display_admin_menu()
            else:
                menu = display_non_admin_menu()
            
            if menu == 'r':
                # Register user - Admin only
                if current_user.role.lower() == "admin":
                    print_header("REGISTER NEW USER")
                    register_user()
                else:
                    print("\n  ERROR: Only Admin users can register new users.\n")
            
            elif menu == 'a':
                # Add task - Available to all
                print_header("ADD NEW TASK")
                add_task()
            
            elif menu == 'va':
                # View all tasks - Now available to all users
                view_all_tasks()
            
            elif menu == 'vm':
                # View my tasks - Available to all
                view_my_tasks()
            
            elif menu == 'vu':
                # View all users - Admin only
                if current_user.role.lower() == "admin":
                    view_all_users()
                else:
                    print("\n  ERROR: Only Admin users can view all users.\n")
            
            elif menu == 'vr':
                # Verify and update roles - Admin only
                if current_user.role.lower() == "admin":
                    verify_and_update_user_roles()
                else:
                    print("\n  ERROR: Only Admin users can verify and update roles.\n")
            
            elif menu == 'dt':
                # Delete task - Admin only
                if current_user.role.lower() == "admin":
                    delete_task()
                else:
                    print("\n  ERROR: Only Admin users can delete tasks.\n")
            
            elif menu == 'vc':
                # View completed tasks - Admin only
                if current_user.role.lower() == "admin":
                    view_completed_tasks()
                else:
                    print("\n  ERROR: Only Admin users can view completed tasks.\n")
            
            elif menu == 'lo':
                # Logout
                print_header("LOGOUT")
                print(f"  Goodbye, {current_user.username}!")
                print()
                user_logged_in = False
            
            elif menu == 'e':
                # Exit
                print_header("THANK YOU")
                print("  Goodbye!!!")
                print()
                exit()
            
            else:
                print("\n  ERROR: You have entered an invalid input. Please try again.\n")


# ===== Program Execution =====
if __name__ == "__main__":
    main()