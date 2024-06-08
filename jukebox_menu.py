from nested_data import albums
# This is the import function to grab code from anothe file
while True:
    print("Please choose your album(invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}: {}: {} "
              .format(index + 1, title, artist, year, songs ))
    for index, value in enumerate(albums):
        title, artist, year, songs = value
        print(index, title, artist, year, songs)
    break
