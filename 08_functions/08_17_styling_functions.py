# Function 1
msgs=['lol', 'lmao', 'rofl', 'jjjj']

def show_messages():
    """Print messages from list"""
    for msg in msgs:
        print(msg)

show_messages()

first=''
last=''
user_info={}

# Function 2
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile = build_profile('micki', 'eustache',
                              location='sinking spring',
                              field='compsci/ viscomm',
                              skill='art')

print(user_profile)

# Function 3
ingredients=[]
def make_sandwich(*ingredients):
    """Builds sandwich based on user input then prints order"""
    user_input = input('\n\nWhat ingredients would you like in your sandwich?:'
                       '\n\t(Separate items with a comma then press enter)\n')
    ingredients=user_input.split(',')
    print(f'\n\nYour sandwich will have: {ingredients}\n\n')

make_sandwich(ingredients)