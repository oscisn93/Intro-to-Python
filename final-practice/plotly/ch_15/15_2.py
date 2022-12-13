# 15-2. Colored Cubes: Apply a colormap to your cubes plot.

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

input_values = [i for i in range(1, 501)]
cubed_values = [i**3 for i in range(1, 501)]

plt.style.use('dark_background') 

plt.scatter(input_values, cubed_values, c=cubed_values, cmap=plt.cm.Blues)
plt.xlabel('numbers')
plt.xlabel('cubed numbers')

gradient = np.linspace(0,2,256)

plt.show()