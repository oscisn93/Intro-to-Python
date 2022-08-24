dinner_list = ['Aristotle', 'Albert Einstein', 'Porfirio Diaz']
invite_message = ',\n\tI would like to invite you to dinner.\n\tPlease let me know if you\'re available!\nRegards,\nOscar\n'

for guest in dinner_list:
    print(guest,invite_message)
    
print('\n',dinner_list[0],' will not be able to make it!\n')
dinner_list[0] = 'Alexander the Great'

for guest in dinner_list:
    print(guest,invite_message)
