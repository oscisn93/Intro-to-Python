fav_nums = {
	'Noemi': [12, 10],
	'Katy': [22],
	'Brandon': [50, 53, 63],
	'Haley': [7, 11],
	'Brenda': [13]
}

for person, num in fav_nums.items():
	nums = ''
	size = len(num)
	if size > 1:
		nums += 's are '
		for i in range(0, size):
			if i == size-1:
				nums += f'and {num[i]}.'
			else:
				nums += f'{num[i]} '
	else:
		nums += f' is {num[0]}'
	print(f'{person}\'s favorite number{nums}')
