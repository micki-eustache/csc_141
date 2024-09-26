users = []

if users == []:
    print('\nMore users needed!\n')
else:
    username = input('\nEnter username:  ')
    if username == users[0]:
        print('Hello admin, would you like to see a status report?\n')
    elif username in users:
        print(f'\nWelcome back {username}!\n')
    elif username not in users:
        print('\nError: user not found.\nPlease contact customer service.\n')