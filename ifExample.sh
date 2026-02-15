#!/bin/bash

# Create if_folder If new_folder exists
if [ -d "new_folder" ]; then
   
    # If-else statement for hyperionDev of new_projects
    if [ -d "if_folder" ]; then
        echo "if_folder exists, i will create hyperionDev."
        mkdir hyperionDev

    else
        echo "if_folder does not exist, i will create new_projects and if_folder."
        mkdir new_projects
        mkdir if_folder
    fi
else 
    echo "new_folder does not exist, i will create it."
    mkdir new_folder
fi      
    