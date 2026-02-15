#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Create a menu and allow the user to make a choice
echo -e "Select an option below by entering a number:\n1 - List files/directories\n2 - Create a file\n3 - Create a folder\n"
read menu

# Validate input
if [[ ! "$menu" =~ ^[1-3]$ ]]; then
    echo "Invalid choice. Please enter 1, 2, or 3."
    exit 1
fi

if [ "$menu" -eq 1 ]; then
    # List the directories and files in the current directory
    ls
elif [ "$menu" -eq 2 ]; then
    # Get the name of the file from the user and create the file
    echo "Enter the name of the file that you want to create"
    read file
    # An if statement is created inside the body of the if statement (nested if statement)
    # Check if the file exists before creating it
    if [ -f "$file" ]; then
        echo "The file named '$file' already exists"
    else
        # Create a new file
        touch "$file"
        echo "File with the name '$file' has been created"
    fi
elif [ "$menu" -eq 3 ]; then
    # Get the name of the folder from the user and create the folder
    echo "Enter the name of the folder that you want to create"
    read folder
    # An if statement is created inside the body of the if statement (nested if statement)
    # Check if the folder exists before creating it
    if [ -d "$folder" ]; then
        echo "The folder named '$folder' already exists"
    else
        # Create a new folder
        mkdir "$folder"
        echo "Folder with the name '$folder' has been created"
    fi
fi