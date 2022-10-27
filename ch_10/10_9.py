def printFile(name):
    try:
        with open(name) as file:
            print(f'\t{name} contents:')
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        pass

printFile('cats.txt')
printFile('dog.txt')