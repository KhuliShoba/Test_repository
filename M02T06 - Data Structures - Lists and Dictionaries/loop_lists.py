# Define a list of my five favorite movies

fav_movies = ["Colombiana", 
                  "Gladiator", 
                  "Avatar", 
                  "Pirates of the Caribbean", 
                  "King Author"
] 
# Loop over the list and print "Movie: " plus the movie's name
for movie in fav_movies:
    print ("Movie: " + movie)

print("-"*30)

# Numbered output using enumerate() to get index (starting from 1)
print("Numbered output:")
for index, movie in enumerate (fav_movies, start=1):
    print(f"Movie {index}: {movie}")