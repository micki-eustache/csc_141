def make_album(artist_name, album_title, song_count = None):
    '''Dictionary builder'''
    album = {'artist': artist_name, 'album_title': album_title}
    # Optional song count only included in dictionary if field is populated
    if song_count:
        album['song_count'] = song_count
    return album
# Quit value
cont = ''

print('Manual Album Entry')
while cont != 'n':
    album = make_album(
        artist_name= input('Enter the artist name:  '),
        album_title= input('Enter the album title:  '),
        song_count= input('(Optional) Enter song count:  ')
    )
    print(album)
    cont = input('Continue? (y/n):  ')
    cont = cont.lower()