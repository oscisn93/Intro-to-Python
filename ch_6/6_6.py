favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

programmers = ['jen', 'sarah', 'edward', 'janet', 'marquis', 'elon', 'mark']

for name in programmers:
    if name in favorite_languages.keys():
        print(f'{name.title()}, thank you for responding')
    else:
        print(f'{name.title()}, you\'re invited to take the quiz!')
