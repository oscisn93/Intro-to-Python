people = [
    {
        'first_name': 'oscar',
        'last_name': 'cisneros',
        'age': 29,
        'city': 'Placentia'
    },
    {
        'first_name': 'peter',
        'last_name': 'ngyuen',
        'age': 39,
        'city': 'Brownsville'
    },
    {
        'first_name': 'jordan',
        'last_name': 'peterson',
        'age': 21,
        'city': 'Montgomery'
    }
]

for person in people:
    first = person["first_name"].title()
    last = person["last_name"].title()
    age = person["age"]
    city = person["city"]
    print(f'{first} {last} is {age} years old and lives in the city of {city}.')
