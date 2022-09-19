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
    print(person["first_name"].title(),person["last_name"].title(),"is",person["age"],"years old and lives in the city of",person["city"])
