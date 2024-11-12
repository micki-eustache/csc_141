class Restaurant:
    """Model of a restaurant"""
  
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print restaurant attributes"""
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        """Print restaurant opening message"""
        print(f"{self.restaurant_name} is open!")

rest1 = Restaurant('Nirvana', 'Indian')
rest2 = Restaurant('Alebrije', 'Mexican')
rest3 = Restaurant("Van's Cafe", "Vietnamese")

rest1.describe_restaurant()
rest1.open_restaurant()

rest2.describe_restaurant()
rest2.open_restaurant()

rest3.describe_restaurant()
rest3.open_restaurant()