# Initialise and empty list to store each line 
Namelist=[]
Doblist=[]

# Open a file and iterate through each line
with open("DOB.txt","r") as G: 
  print("NAME")
  print("--------------------")
  print()

  # Split and store the name list
  for line in G:
    store=line.split(" ",2)

    # Print the split name list
    print (store[0]+" "+store[1]+"\n")

    # Open a file and iterate through each line
with open("DOB.txt","r") as G: 
 print("DATE OF BIRTH")
 print("----------------------")
 print()

 # Split and store the birthdate list
 for line in G:
    store=line.split(" ",2)
    # Print the split birthdate list
    print (store[2])