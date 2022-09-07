cities = ['Riverside', 'Corona', 'Anaheim']
age_cohorts = ['18-20', '21-25', '26+']
composite = [f'{city} {age}' for city in cities for age in age_cohorts ]
for comp in composite:
    print(comp)
