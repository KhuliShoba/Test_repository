#!/bin/bash

# Create 3 folders named myCd1, myCd2, and myCd3
mkdir myCd1
mkdir myCd2
mkdir myCd3

# Navigate into myCd1
cd myCd1

# Create 3 new folders inside myCd2
mkdir myCd2/subfolder1
mkdir myCd2/subfolder2
mkdir myCd2/subfolder3

#remove two of the subfolders
rm -rf myCd2/subfolder1
rm -rf myCd2/subfolder2

# List the contents of the myCd2 directory
cd myCd2       
ls 

