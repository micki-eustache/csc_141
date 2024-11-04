def make_album(artist_name, album_title, song_count = None):
    '''Dictionary builder'''
    album = {'artist': artist_name, 'album_title': album_title}
    # Optional song count only included in dictionary if field is populated
    if song_count:
        album['song_count'] = song_count
    return album

# Create and print entries
album = make_album(artist_name='Childish Gambino', 
           album_title='Bando Stone and The New World')
print(album)
album = make_album(artist_name='Tyler, the Creator', 
           album_title='Chromakopia')
print(album)
album = make_album(artist_name='Caravan Palace', 
           album_title='<|°_°|>',
           song_count= 11)
print(album)