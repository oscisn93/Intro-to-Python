import json

def writeFavNumToJSON():
    name: str = input('Enter your name please: ')
    number: float = float(input('What is your favorite number? '))
    user = {
        'name': name,
        'fav_num': number 
    }
    user_json = json.dumps(user)
    with open('users.json', 'a') as json_file:
        json_file.write(user_json)

writeFavNumToJSON()