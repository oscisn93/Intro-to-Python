import os

ASSIGNMENT_NUMS = [1,2,3,4,5,6,7,8,10]
CHAPTER = '15'

os.mkdir(f'ch_{CHAPTER}')
os.chdir(f'ch_{CHAPTER}')

for num in ASSIGNMENT_NUMS:
   filename = f'{CHAPTER}_{num}.py'
   file = open(filename, 'x')
   file.close()
