import os

ASSIGNMENT_NUMS = [1,2,3]
CHAPTER = '11'

os.mkdir(f'ch_{CHAPTER}')
os.chdir(f'ch_{CHAPTER}')

for num in ASSIGNMENT_NUMS:
   filename = f'{CHAPTER}_{num}.py'
   file = open(filename, 'x')
   file.close()
