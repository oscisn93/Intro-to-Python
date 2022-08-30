#3-7. Shrinking Guest List:

dinner_list = ['Aristotle', 'Albert Einstein', 'Porfirio Diaz']
invite_message = ',\n\tI would like to invite you to dinner.\n\tPlease let me know if you\'re available!\nRegards,\nOscar\n'

for guest in dinner_list:
    print(guest, invite_message)

print('\n',dinner_list[0],' will not be able to make it!\n')
dinner_list[0] = 'Alexander the Great'

for guest in dinner_list:
    print(guest, invite_message)

print('I found a bigger table for dinner!\n')
dinner_list.insert(0, 'Paul Walker')
dinner_list.insert(2, 'Bruce Lee')
dinner_list.append('Ariel Camacho')

for guest in dinner_list:
    print(guest, invite_message)

print('\nCurrently I am inviting ',len(dinner_list),' guests to dinner.\nHowever I can only invite two now!\n')

sorry_message = 'Sorry, I can\'t have you over for dinner after all!\n'  
print('Hey, ',dinner_list.pop(),',\n',sorry_message)
print('Hey, ',dinner_list.pop(),',\n',sorry_message)
print('Hey, ',dinner_list.pop(),',\n',sorry_message)
print('Hey, ',dinner_list.pop(),',\n',sorry_message)

for guest in dinner_list:
    print(guest, invite_message)

dinner_list.remove(dinner_list[0])
del dinner_list[0]
print(dinner_list)
