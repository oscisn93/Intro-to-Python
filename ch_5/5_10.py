current_users = ['admin', 'Jaden', 'Matt',  'Alex', 'Judy']
new_users = ['Alex', 'Paolo', 'Jaylen', 'Matthew', 'Judith']
for new_user in new_users:
    available = True
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            available = False
    if available:
        print('username',new_user,'is available!')
    else:
        print(new_user,'unavailable: please pick a different username!')
