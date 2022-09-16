# TODO: make path variable so we can select
# the file programmatically and run program
# from util folder

ASSIGNMENT_NUMS = [1,2,3,5,6,7,10,11]
CHAPTER = '6'


for num in ASSIGNMENT_NUMS:
   filename = f'{CHAPTER}_{num}.py'
   file = open(filename, 'x')
   file.close()
