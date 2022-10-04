famous_people =[
    {
        'name': 'Pancho Villa',
        'birthdate': 'unknown',
        'birthplace': 'Durango',
        'quote': '\"We don\'t want any Spaniards here.\"'
    },
    {
        'name': 'Alexander the Great',
        'birthdate': 'unknown',
        'birthplace': 'Macedonia',
        'quote': '\"Give me your land!\"'
    },
    {
        'name': 'Emiliano Zapata',
        'birthdate': 'unknown',
        'birthplace': 'Morelia',
        'quote': '\"I\'d rather die on my feet than live on my knees\"'
    }
]

print('{0:<20s} {1:<10s} {2:<10s} {3:<15s}'.format('Name', 'Birthdate', 'Birthplace', 'Quote'))
print('{0:-^80s}'.format(''))
for person in famous_people:
    print('{0:<20s} {1:<10s} {2:<10s} {3:<15s}'.format(person['name'], person['birthdate'], person['birthplace'], person['quote']))