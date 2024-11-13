from folder2.city_functions import *

city = input('Enter city name:  ')
country = input('Enter country name:  ')
pop = input('Enter population:  ')

formatted_city_country = format_city_country(city, country)
print(formatted_city_country)