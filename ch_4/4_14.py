from http import server


print('All users: ')
all_users = ['admin', 'isaac', 'zach']
for user in all_users:
    print(user)

all_users.append('mary')

print('\nUntrusted users: ')
untrusted_users = ['mary', 'marquis']
for user in untrusted_users:
    print(user)
    
print('\nTrusted users: ')
trusted_users = [user for user in all_users if user not in untrusted_users]
for trusted in trusted_users:
    print(trusted)

all_users = {'admin', 'isaac', 'zach', 'mary', 'marquis'}
untrusted_users = {'marquis', 'leana'}
trusted_users = all_users.difference(untrusted_users)
print('\nTrusted users set: ')
for user in trusted_users:
    print(user)
