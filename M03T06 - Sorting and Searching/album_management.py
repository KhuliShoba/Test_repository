# Design a class called Album that has the following attributes:
# - album_name: a string representing the album title
# - number_of_songs: an integer representing the number of tracks in the album
# - album_artist: a string representing the artist name
class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"{self.album_name} by {self.album_artist} with {self.number_of_songs} tracks"
# Create a list of Album objects with at least 5 different albums.
albums1 = [
    Album("Thriller", 9, "Michael Jackson"),
    Album("Back in Black", 10, "AC/DC"),
    Album("The Dark Side of the Moon", 10, "Pink Floyd"),
    Album("The Bodyguard", 12, "Whitney Houston"),
    Album("Rumours", 11, "Fleetwood Mac")
]
# Write a function that takes a list of Album objects and returns a new list sorted by number_of_songs.
def sort_albums_by_tracks(albums):
    return sorted(albums, key=lambda album: album.number_of_tracks)
print("Albums sorted by number of tracks:")
for album in sort_albums_by_tracks(albums1):
    print(album)
# Swap the element at position 1 of albums1 with the element at position 2 and print it out.
albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nAlbums after swapping index 0 and 1:")
for album in albums1:
    print(album)
# Add five Album objects to the second album list, and print out the list.
albums2 = [
    Album("Hotel California", 9, "Eagles"),
    Album("Abbey Road", 17, "The Beatles"),
    Album("Led Zeppelin IV", 8, "Led Zeppelin"),
    Album("Sgt. Pepper's Lonely Hearts Club Band", 13, "The Beatles"),
    Album("Born in the U.S.A.", 12, "Bruce Springsteen")
]
print("\nAlbums in albums2:")
for album in albums2:
    print(album)
    # Copy all of the albums from albums1 into albums2.
albums2.extend(albums1)
print("\nAlbums in albums2 after copying from albums1:")
for album in albums2:
    print(album)
   # Add the following two albums to albums2:
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))
print("\nAlbums in albums2 after adding two more albums:")
for album in albums2:
    print(album)    
    # Sort the albums in albums2 alphabetically according to the album name and print out the sorted list.
sorted_albums = sorted(albums2, key=lambda album: album.title)
print("\nAlbums sorted alphabetically by album name:")
for album in sorted_albums:
    print(album)    
# Search for the album Dark Side of the Moon in albums2 and print out the index of the album in the albums2 list.
search_title = "Dark Side of the Moon"
index = next((i for i, album in enumerate(albums2) if album.title == search_title), None)
if index is not None:
    print(f"\nThe album '{search_title}' is found at index: {index}")
else:
    print(f"\nThe album '{search_title}' is not found in albums2.")
