cubes = [i**3 for i in range(1, 11)]

print('\nThe first three items in the list are: ')
for i in cubes[0:3]:
    print(i)

print('\nThree items from the middle of the list are: ')
for i in cubes[3:6]:
    print(i)

print('\nThe last three items in the list are: ')
for i in cubes[7:]:
    print(i)
