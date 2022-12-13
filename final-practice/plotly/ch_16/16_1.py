import csv
from matplotlib import pyplot as plt

csv_file = 'data/sitka_weather_2018_simple.csv'
with open(csv_file) as data:
    rainfall_data = [row['PRCP'] for row in csv.DictReader(data)]
    plt.plot(rainfall_data)
    plt.yticks(rotation=45)
    plt.show()
