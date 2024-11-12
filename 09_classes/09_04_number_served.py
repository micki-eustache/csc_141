class Restaurant:
    """Model of a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Print restaurant attributes"""
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        """Print restaurant opening message"""
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self):
        """Assign value to number served"""
        self.number_served = int(input("Set number served:  "))

    def increment_number_served(self, customers):
        """Add to the number served"""
        self.number_served += customers

restaurant = Restaurant('Nirvana', 'Indian')

print(restaurant.number_served)

restaurant.number_served = 1
print(restaurant.number_served)

restaurant.set_number_served()
print(restaurant.number_served)

restaurant.increment_number_served(4)
print(restaurant.number_served)
