# TODO: make path variable so we can select
# the file programmatically and run program
# from util folder

import os
# import sys

ASSIGNMENT_NUMS = [8,9,10,11,12]
CHAPTER = '5'

path_to_files = f'{os.path}../ch_'

for num in ASSIGNMENT_NUMS:
   filename = f'{path_to_files}{CHAPTER}/{CHAPTER}_{num}.py'
   file = open(filename, 'x')
   file.close()
