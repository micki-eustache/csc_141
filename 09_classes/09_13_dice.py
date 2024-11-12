
from random import randint as r

class Die:
    """Model of dice"""

    def __init__(self, sides=6):
        """Initialize die attributes"""
        self.sides = sides
        
    def roll_die(self):
        """Method to roll die and get randome number"""
        print(r(1, self.sides))

print('D6--------------------------')
d6 = Die()
for num in range(10):
    d6.roll_die()

print('\nD10-------------------------')
d10 = Die(10)
for num in range(10):
    d10.roll_die()

print('\nD20-------------------------')
d20 = Die(20)
for num in range(10):
    d20.roll_die()