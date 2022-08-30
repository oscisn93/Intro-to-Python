# create and print a raw pyrhon list 
locations = ['Mexico City', 'Mazatlan', 'Tokyo', 'Helsinki', 'Reykjavic']
print('The contents of the list: ',locations)
# print a sorted list without altering the original
print('The sorted contents of the list: ',sorted(locations))
print('The original contents of the list: ',locations)
# print a reverse sorted list without altering the original
print('The reversed contents of the list: ',sorted(locations, reverse=True))
print('The original contents of the list: ',locations)
# reverse the original list
locations.reverse()
print('The reversed contents of the list: ',locations)
# reverse list but first remove the alphabetically first element
locations.reverse()
locations.remove(sorted(locations)[0])
print('The original contents of the list after removing the alphabetically first element: ',locations)
# sort the original list
locations.sort()
print('The sorted contents of the list: ',locations)
# sort the original list in reverse
locations.sort(reverse=True)
print('The reverse sorted contents of the list: ',locations)
