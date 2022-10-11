import os

ASSIGNMENT_NUMS = [6,7,8,9,10,11,12]
CHAPTER = '10'

os.mkdir(f'ch_{CHAPTER}')
os.chdir(f'ch_{CHAPTER}')

for num in ASSIGNMENT_NUMS:
   filename = f'{CHAPTER}_{num}.py'
   file = open(filename, 'x')
   file.close()
