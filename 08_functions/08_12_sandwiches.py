ingredients = []
def make_sandwich(*ingredients):
    '''Sandwich builder. Prints order'''
    user_input = input('\n\nWhat ingredients would you like in your sandwich?:'
                       '\n\t(Separate items with a comma then press enter)\n')
    ingredients = user_input.split(',')
    print(f'\n\nYour sandwich will have: {ingredients}\n\n')

make_sandwich(ingredients)