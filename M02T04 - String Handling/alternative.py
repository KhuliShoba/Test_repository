# Request the user to input a sentence
sentence = input("Enter your sentence: ")

# Create an empty string 
new_sentence = ""

# Iterate through the string using the index
for i in range(len(sentence)):
    if i % 2 == 0:
        # If the index is even make it uppercase
        new_sentence += sentence[i].upper()
    else:
        # If the index is odd make it lowercase
       new_sentence += sentence[i].lower()

# Print the final result
print(f"Modofied sentence: {new_sentence}")

