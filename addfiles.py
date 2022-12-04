import os

ASSIGNMENT_NUMS = ['1','2a','2b','4','5','7','8']
CHAPTER = '16'

os.mkdir(f'ch_{CHAPTER}')
os.chdir(f'ch_{CHAPTER}')

for num in ASSIGNMENT_NUMS:
   filename = f'{CHAPTER}_{num}.py'
   file = open(filename, 'x')
   file.close()
