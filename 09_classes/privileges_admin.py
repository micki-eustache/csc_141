import users

class Admin(users.User):
    """Model of a specific type of user"""

    def __init__(self, first_name, last_name, user_id, age, state):
        """Initialize attributes of the parent class"""
        super().__init__(first_name, last_name, user_id, age, state)
        self.privileges = Privileges()

class Privileges:
    def __init__ (self):
        self.privileges = ['add post', 'delete post', 
                      'ban user', 'restrict user']
    
    def show_privileges(self):
        """Display admin privileges"""
        print(self.privileges)
