rivers = {
    'nile': 'egypt',
    'seine': 'france',
    'ganges': 'india'
}

for river, location in rivers.items():
    print(f'\nThe {river.title()} river runs through {location.title()}')
    print({river})
    print({location})