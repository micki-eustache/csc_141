vacations = {}
polling_active = True

while polling_active:
    user = input('Enter your name:  ')
    vacay = input("What's your dream vacation?  ")
    vacations[user] = vacay

    cont = input('Anyone else want to participate in our poll? (y/n)')
    if cont == 'n':
        polling_active = False
    