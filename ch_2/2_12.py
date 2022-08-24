# Oscar Cisneros
# Print a message that displays the circumference and area of a circle
# based on a specific radius, rounded to two decimal places.

from math import pi

r = 12
area = pi* r ** 2
print ("The are of a circle with radius",r,"is",round(area, 2))

circumference = 2 * pi * r
print("The circumference of a circle of radius",r," is ", round(circumference, 2))
