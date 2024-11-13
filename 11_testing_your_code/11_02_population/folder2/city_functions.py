def format_city_country(city, country, pop=None):
    """Format city, country and population as a single string"""
    city_country = f'{city}, {country}' 
    if pop != None:
        city_country += f' - Population {pop}'
    return city_country.title()
