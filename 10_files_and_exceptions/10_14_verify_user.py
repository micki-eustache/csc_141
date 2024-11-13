from pathlib import Path
import json

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        username = user_info['username']
        return username
    else:
        return None

def get_new_userinfo(path):
    """Prompt for a new username."""
    user = {}
    user['username'] = input('Enter your username:  ')
    user['dob'] = input('Enter your date of birth (mmddyy):  ')
    user['state'] = input('Enter your state abbreviated:  ').upper()
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        cont = input(f'Continue as {username}? (y/n):  ').lower()
        if cont == 'n':
            user_info = get_new_userinfo(path)
            print(f"We'll remember you when you come back, {user_info['username']}!")
        if cont == 'y':
            print(f"Welcome back, {username}!")

greet_user()