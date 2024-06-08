albums = [
    ("welcome to my nightmare ", "Allice Cooper", 1975), 
    ("Bad Company", "Bad Company", 1974),
    ("Night Flight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]
print(len(albums))

for album, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(album, artist, year))
# Unpacking tuples to return the values for album, artist, year





