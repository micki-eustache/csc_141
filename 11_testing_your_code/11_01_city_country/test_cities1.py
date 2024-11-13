from folder1.city_functions import format_city_country

def test_city_country():
    """Will it work with just city and country?"""
    formatted_city_country = format_city_country('santiago', 'chile')
    assert formatted_city_country == 'Santiago, Chile'
