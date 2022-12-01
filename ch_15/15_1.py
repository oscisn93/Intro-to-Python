# 15-1. Cubes: A number raised to the third power is a cube.
# Plot the first 5000 cubic numbers.
# Display the graph as a blue line.s
import matplotlib.pyplot as plt
import numpy as np

input_values = [i for i in range(1, 501)]
cubed_values = [i**3 for i in range(1, 501)]

plt.style.use('dark_background')

plt.plot(input_values, cubed_values)
plt.xlabel('numbers')
plt.xlabel('cubed numbers')

gradient = np.linspace(0, 2, 256)

plt.show()
