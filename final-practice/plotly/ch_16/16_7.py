import json
import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
metadata_title = ""
with open(filename) as f:
    all_eq_data = json.load(f)
    
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
metadata_title = all_eq_data['metadata']['title']
print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []  # new code here
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title'] 	# new code here
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)		# new code here


print(mags[:10])
print(lons[:10])
print(lats[:10])

# Map the earthquakes. 
data = [{
       'type': 'scattergeo',
       'lon': lons,
       'lat': lats,
       'text': hover_texts,		# new code here
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,						
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
       },
   }]

my_layout = Layout(title=metadata_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')