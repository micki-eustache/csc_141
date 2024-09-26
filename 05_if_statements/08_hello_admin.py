users = ['admin', 'mtma0327', 'jaden99', 'GGgio', 'yunluvr']

username = input('\nEnter username:  ')
if username == users[0]:
    print('\nHello admin!\nWould you like to see a status report?\n')
elif username in users:
    print(f'\nWelcome back {username}!\n')
elif username not in users:
    print('\nError: user not found.\nPlease contact customer service.\n')