print(" x   x**2 x**3")
for x in range(1, 11):
    x_squared = x**2
    x_cubed = x**3
    print(' {0:<3d} {1:<3d} {2:<4d}'.format(x, x_squared, x_cubed))