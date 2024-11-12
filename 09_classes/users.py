class User:
    """Model of users"""
   
    def __init__(self, first_name, last_name, user_id, age, state):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.age = age
        self.state = state

    def describe_user(self):
        """Display all stored infor about user"""
        print(f"\nName: {self.first_name.title()} {self.last_name.title()}    "
              f"\nUser ID: {self.user_id}    Age: {self.age}    "
              f"State: {self.state}")

    def greet_user(self):
        """Print greeting message to user"""
        print(f"Welcome back {self.first_name.title()}!\n")