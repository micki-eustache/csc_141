from folder2.city_functions import format_city_country

def test_city_country():
    """Will it work with just city and country?"""
    formatted_city_country = format_city_country('santiago', 'chile')
    assert formatted_city_country == 'Santiago, Chile'

def test_city_country_pop():
    """Will it work with expected data?"""
    formatted_city_country_pop = format_city_country('santiago', 'chile', 6113930)
    assert formatted_city_country_pop == 'Santiago, Chile - Population 6113930'