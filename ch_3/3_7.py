"""3-7. Shrinking Guest List:
You just found out that your new dinner table won't arrive in time for the dinner,
and you have space for only two guests.

Use len() to print a message indicating the number of people you are inviting to dinner.
Add a new line that prints a message saying that you can invite only two people for dinner.
Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list,
print a message to that person letting them know you're sorry you can't invite them to dinner.
Print a message to each of the two people still on your list,
letting them know they're still invited.
Use remove to remove the second to last name.
Use del to remove the last name from your list,
so you have an empty list.
Print your list to make sure you actually have an empty list at the end of your program.
"""

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
delete(dinner_list[0])
print(dinner_list)
