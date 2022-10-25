# Wrap your code from 10-6 in a while loop so the user
# can continue entering numbers even if they make a mistake
# and enter text instead of a number.

def add_nums():
    print('Follow the prompt instructions to get the sum of two numbers!')
    try:
        num_1 = int(input("Enter a number: "))
        num_2 = int(input("Please enter another number: "))
        print('the sum is',num_1+num_2)
    except ValueError:
        print('The last number you entered was invalid!')

add_nums()