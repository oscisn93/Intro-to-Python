import json

def writeFavNumToJSON():
    name: str = input('Enter your name please: ')
    number: float = float(input('What is your favorite number? '))
    user = {
        'name': name,
        'fav_num': number 
    }
    user_json = json.dumps(user)
    with open('users.json', 'w') as json_file:
        json_file.write(user_json)

def printFavNumFromJSON():
    with open('users.json', 'r') as json_file:
        data = json_file.read()
        data = json.loads(data)
        if 'name' in data:
            name = input('Enter your name please: ')
            if data['name'] == name:
                print(data['name'], 'I know your favorite number! It\'s',data['fav_num'])
                return
        writeFavNumToJSON()

printFavNumFromJSON()
