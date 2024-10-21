favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

names = ['jen', 'sarah', 'edward', 'phil', 'tim', 'dave', 'astra']

for name in names:
    if name in favorite_languages:
        print(f'\nThank you for answering the poll, {name.title()}.')
    else:
        print(f'\n{name.title()}, please answer the poll.')