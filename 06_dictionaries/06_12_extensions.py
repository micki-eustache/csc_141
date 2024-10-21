cities = {
    'Glenside': {'name': 'Glenside', 'state': 'PA'},
    'Sinking Spring': {'name': 'Sinking Spring', 'state': 'PA'},
    'Madison': {'name': 'Madison', 'state': 'NJ'},
}

people = {
    'MagKli': {'first_name': 'Maggie', 'last_name': 'Kline', 'age': 21, 'city': cities['Glenside']},
    'MicEus': {'first_name': 'Micki', 'last_name': 'Eustache', 'age': 20, 'city': cities['Sinking Spring']},
    'JonPen': {'first_name': 'Jonathan', 'last_name': 'Pensado', 'age': 22, 'city': cities['Sinking Spring']},
    'FinJac': {'first_name': 'Finn', 'last_name': 'Jackson', 'age': 20, 'city': cities['Madison']}
}

pets = {
    'LucEus': {'name': 'Lucii', 'type': 'cat', 'owner': people['MagKli'], 'sex': 'F'},
    'PepKli': {'name': 'Pepper', 'type': 'cat', 'owner': people['MicEus'], 'sex': 'F'},
    'VolPen': {'name': 'Volpi', 'type': 'dog', 'owner': people['JonPen'], 'sex': 'F'},
    'BarJac': {'name': 'Barnaby', 'type': 'cat', 'owner': people['FinJac'], 'sex': 'M'}
}

for pet, owner in pets.items():
    print(f'\n{pet, owner}')