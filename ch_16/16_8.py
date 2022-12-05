import json
from datetime import datetime
from matplotlib import pyplot as plt
import numpy as np

filename = 'data/deathsbystateovertime.json'

with open(filename) as f:
    covid_data = json.load(f)
    territories = []
    dates = []
    deaths = []
    for row in covid_data['data']:
        territory = row[9]
        # create a date from only the first 10 characters of the string
        date = datetime.strptime(row[8][:10], '%Y-%m-%d').date()
        daily_deaths = int(row[15])
        if territory not in territories:
            territories.append(territory)
            dates.append([date])
            deaths.append([daily_deaths])
        else:
            dates[-1].append(date)
            deaths[-1].append(daily_deaths)
    dates = dates[0]

x_axis = np.arange(len(dates))
print(x_axis)
width = 1/len(x_axis)

for i in range(len(territories)):
    colors  = ['r','b', 'g']
    plt.bar(x_axis + width*i, deaths[i], color=colors[i%3],width=width, edgecolor='black', label=territories[i])

plt.xlabel("Deaths by territory")
plt.ylabel("Number of deaths")
plt.title("Number of covid deaths by by US territory")

plt.xticks(x_axis+width/2, dates, rotation=45)
plt.legend()

plt.show()
