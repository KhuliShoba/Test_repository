# Save a sentence below as the long string#
sentence="The!quick!brown!fox!jumps!over!the!lazy!dog."
# Print the saved sentence#
print(sentence)
# In the centence replace the "!" with empty spaces" " using the replace() function. 
sentence=sentence.replace("!"," ")
# Reprint the sentence "The quick brown fox jumps over the lazy dog."
print("sentence.replace(""!""," "):{}".format(sentence))
# In the sentence convert the lower case into upper case using the upper() function#
sentence=sentence.upper()
# Reprint the sentece in upper case#
print(f"sentence.upper():{sentence}")
# print the sentence in reverse#
print(sentence[: :-1])