cities = {
    'Los Angeles': {
        'country': 'the United States of America',
        'population': '3,919,973',
        'fact': 'it was originally home to the Chumash and Tongva indigenous peoples, but was claimed by Juan Rodríguez Cabrillo for Spain in 1542.'
    },
    'Monterrey': {
        'country': 'the United Mexican States',
        'population': '1,142,194',
        'fact': 'Monterrey is one of the most livable cities in Mexico, and a 2018 study found that suburb San Pedro Garza García is the city with the best quality of life in Mexico.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '13,988,129',
        'fact': 'Tokyo was originally a village called Edo, in what was formerly part of the old Musashi Province.'
    }
}

for city, info in cities.items():
    city_string = f'The city of {city} is in the country of {info["country"]}.\nIt has a population of {info["population"]}.\nA little known fact is that {info["fact"]}\n'
    print(city_string)
