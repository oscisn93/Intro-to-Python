#  Starting with your program from 10-10,
# modify it such that it can take a word from the user 
# and search the book for the number of occurrences of that word.

import os
from urllib.error import HTTPError
import wget

url = "https://gutenberg.org/files/2701/2701-0.txt"
try:
    filename = wget.download(url)
except HTTPError:
    print("That url is invalid or no longer has the resource you are requesting.")

try:
    with open(filename) as book:
        word = input('\nEnter a word to look up in the text:')
        word_count = book.read().split().count(word)
        print("\nThe word \"",word,"\" is used approximately",word_count,"times.")
    os.remove(filename)
except NameError:
    pass