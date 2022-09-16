rivers = {
    'Amazon': 'Brazil',
    'Mississippi': 'The United States',
    'Danube': 'Romania'
}

for river, country in rivers.items():
    print(f'The {river} River primarily runs through {country}.')

for river in rivers.keys():
    print('The',river,'River')

for country in rivers.values():
    print(country)
