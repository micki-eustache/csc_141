vacations = {}
polling_active = True

while polling_active:
    user = input('\tEnter your name:  ')
    vacay = input("\tWhat's your dream vacation?  ")
    vacations[user] = vacay

    cont = ''
    while cont != 'y':
        cont = input('\nAnyone else want to participate in our poll? (y/n)')
        cont = cont.lower()
        if cont == 'n':
            polling_active = False
            break
        elif cont == 'y':
            polling_active = True
        else:
            print('\tError. Please enter valid input.')

print('\n')
for user, vacay in vacations.items():
    print(f'{user.title()} would like to go to {vacay.title()}.')