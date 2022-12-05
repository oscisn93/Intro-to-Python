import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

def get_temp_indices(header_row):
    high = header_row.index('TMAX')
    low = header_row.index('TMIN')
    return high, low

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    high_low_indices = get_temp_indices(header_row)
    station_name = ""
    
    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        station_name = row[1]
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:													# new code
            high = int(row[high_low_indices[0]])
            low = int(row[high_low_indices[1]])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, highs, c='red', alpha=0.5)  # new code
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = f"Daily high and low temperatures - 2018\n{station_name}"
ax.set_title(title, fontsize=20)

ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

highest = max(highs)+10
lowest = min(lows)-10
plt.ylim(lowest, highest)

plt.show()