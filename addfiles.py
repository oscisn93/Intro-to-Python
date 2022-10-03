# TODO: make path variable so we can select
# the file programmatically and run program
# from util folder

ASSIGNMENT_NUMS = [1,2,3,4,6,7,9,10,11,12,13,14,15]
CHAPTER = '9'


for num in ASSIGNMENT_NUMS:
   filename = f'{CHAPTER}_{num}.py'
   file = open(filename, 'x')
   file.close()
