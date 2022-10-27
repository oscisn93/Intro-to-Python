def printFile(name):
    try:
        with open(name) as file:
            print(f'\t{name} contents:')
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f'Sorry, but the file {name} does not exist.')

printFile('cats.txt')
printFile('dogs.txt')