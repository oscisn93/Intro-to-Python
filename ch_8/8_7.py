def make_album(artist_name, album_title, no_songs=None):
    return {
        "name" : artist_name,
        "album" : album_title,
        "number_songs" : no_songs
    }

print(make_album("Pantera", "Vulgar Display of Power"))
print(make_album("Slayer", "Divine Intervention"))
print(make_album("Lamb of God", "Resolution"))

print(make_album("Lamb of God", "Ashes of the Wake", 10))
