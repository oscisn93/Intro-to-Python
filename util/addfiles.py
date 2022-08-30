# TODO: make path variable so we can select
# the file programmatically and run program
# from util folder

ASSIGNMENT_NUMS = [8,9,10,11,12]
CHAPTER_PREFIX = '5_'

for num in ASSIGNMENT_NUMS:
    filename = f'{CHAPTER_PREFIX}{num}.py'
    file = open(filename, 'x')
    file.close()
