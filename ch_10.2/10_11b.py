import json

def printFavNumFromJSON():
    with open('users.json', 'r') as json_file:
        data = json_file.read()
        data = json.loads(data)
        print(data['name'], 'I know your favorite number! It\'s',data['fav_num'])

printFavNumFromJSON()