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

restaurant = Restaurant('Nirvana', 'Indian')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()