from pathlib import Path
import json

def get_stored_username():
    """Get stored username if available."""
    path = Path('username.json')
    if path.exists():
        with open(path, 'r') as file:
            return json.load(file)
    else:
        return None

def get_new_username():
    """Prompting for a new username."""
    username = input("What is your name? ")
    path = Path('username.json')
    with open(path, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    """Greet the user by name."""
    stored_username = get_stored_username()
    if stored_username:
        username = input(f"Is {stored_username} your username? (yes/no) ")
        if username.lower() == 'yes':
            print(f"Welcome back, {stored_username}!")
        else:
            stored_username = get_new_username()
            print(f"We'll remember you when you come back, {stored_username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()


