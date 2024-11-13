from pathlib import Path

guests = ''
guest = ''

while guest != '0':
    guest = input('(Enter 0 to quit)\nEnter name, press enter, repeat: ')
    if guest == '0':
        break
    else: 
        guests += guest + '\n'

path = Path('guest_book.txt')
path.write_text(guests)