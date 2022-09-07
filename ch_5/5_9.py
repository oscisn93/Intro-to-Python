usernames = []
if len(usernames) >= 1:
    for username in usernames: 
        if username == 'admin':
            print('Hello ',username,'\nWould you like a status report?')
        else:
            print('Hello ',username,'\nNo status report for you normie!')
else:
    print('We need to find users first!')
