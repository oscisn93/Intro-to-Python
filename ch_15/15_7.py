# 15-7. Three Dice: 
# When you roll three D6 dice, the smallest number 
# you can roll is 3 and the largest number is 18. 
# Create a visualization that shows what happens when you roll three D6 dice.  
# Adjust everything that needs to be adjusted.

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create three D6 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(10_000_000): #increase to 50,000
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 dice 10 million times',
           xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6x3.html')