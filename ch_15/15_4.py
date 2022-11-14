# 15-4. Modified Random Walks: Start with the program from 15-3.  
# Create a copy of the RandomWalk class called RandomWalk1 still within the file random_walk.py.  
# In the RandomWalk1 class, x_step and y_step are generated from the same set of conditions. 
# The direction is chosen randomly from the list [1, -1] and the distance from the list [0, 1, 2, 3, 4]. 
# Modify the values in these lists to see what happens to the overall shape of your walks. 
# Try a longer list of choices for the distance, such as 0 through 8, or remove the –1 from the x or y direction list.  
# Turn in the most unusual result you find.

import matplotlib.pyplot as plt
from random_walk import RandomWalk1

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk1(5_000)
    rw.fill_walk()
 
    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)  # size changed here
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolor='none', s=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.plot(rw.x_values, rw.y_values, lw=1)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break