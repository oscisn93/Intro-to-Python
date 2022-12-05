import json
from datetime import datetime

filename = 'data/deathsbystateovertime.json'

with open(filename) as f:
    covid_data = json.load(f)
    territories = []
    for row in covid_data['data']:
        territory = row[9]
        # create a date from only the first 10 characters of the string
        date = datetime.strptime(row[8][:10], '%Y-%m-%d')
        if territory not in territories:
            territories.append(territory)
    print(len(territories))