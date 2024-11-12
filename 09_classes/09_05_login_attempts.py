class User:
    """Model of users"""
    
    def __init__(self, first_name, last_name, user_id, age, state):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.age = age
        self.state = state
        self.login_attempts = 0

    def describe_user(self):
        """Display all stored infor about user"""
        print(f"\nName: {self.first_name.title()} {self.last_name.title()}    "
              f"\nUser ID: {self.user_id}    Age: {self.age}    "
              f"State: {self.state}")

    def greet_user(self):
        """Print greeting message to user"""
        print(f"Welcome back {self.first_name.title()}!\n")

    def increment_login_attempts(self):
        """Add 1 to login_attempts with each login attempt"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Set login attempts back to 0"""
        self.login_attempts = 0

user1 = User('Michael', 'Liminar', 'MLim', 30, 'PA')
user2 = User('Cologne', 'Clover', 'CCC0327', 21, 'DC')
user3 = User('Quinn', 'Vinisala', 'UiRrinVin', 20, 'DC')
user4 = User('Atlas', 'Cathenin', 'adlasfun', 18, 'NJ')

print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)