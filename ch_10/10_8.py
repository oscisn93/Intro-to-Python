# Make two files, cats.txt and dogs.txt. 
# Store at least three names of cats in the first file and three names of dogs in the second file. 
# Write a program that tries to read these files and print the contents of the file to the screen. 
# Wrap your code in a try-except block to catch the FileNotFound error, 
# and print a friendly message if a file is missing. 
# Temporarily rename each of your files, 
# and make sure the code in the except block executes properly.  
# Make sure an exception is caught for either file missing.

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