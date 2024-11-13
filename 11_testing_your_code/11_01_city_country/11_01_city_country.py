from folder1.city_functions import format_city_country

city = input('Enter city name:  ')
country = input('Enter country name:  ')

formatted_city_country = format_city_country(city, country)
print(formatted_city_country)