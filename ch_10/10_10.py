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
        the_count = book.read().split().count('the')
        print("\nThe word \"the\" is used approximately",the_count,"times.")
    os.remove(filename)
except NameError:
    pass
