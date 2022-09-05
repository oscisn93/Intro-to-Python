**4-1. Pizzas:**
Think of at least three kinds of your favorite pizza. 
Store these pizza names in a list, and then use a for loop to print the name of each pizza.
Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza.
For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
Add a line at the end of your program, outside the for loop, that states how much you like pizza.
The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

**4-3. Counting to Twenty:**
Use a for loop to print the numbers from 1 to 20, inclusive.

**4-4. One Million:**
Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

**4-5. Summing a Million:**
Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

**4-6. Odd Numbers:**
Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

**4-8. Cubes:**
A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

**4-9. Cube Comprehension:**
Use a list comprehension to generate a list of the first 10 cubes.

**4-10. Slices:**
Starting with program 4-9, add several lines to the end of the program that do the following:
Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
Print the message The last three items in the list are:. Use a slice to print the last three items in the list.

**4-11. My Pizzas, Your Pizzas:**
Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. 
Then, do the following:
Add a new pizza type to the original list.
Add a different pizza type to the list friend_pizzas.
Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

**4-13. Buffet:**
A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
Use a for loop to print each food the restaurant offers.
Try to modify one of the items, and make sure that Python rejects the change.
The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

**4-14. Trusted Users:**
Create a list called all_users and initialize it with three users.  Print it.
Add a user to this list using append
Create a list called untrusted_users with two users, one in all_users and one that is not.  Print it.
Using the two previously created lists, create a list called trusted_users 
using a list comprehension
using a for loop
**Sets:**
Create a set called all_user with 5 user names.
Create a set called untrusted_users containing 2 users, one in all_users and one not in all_users.
Using subtraction, create a set called trusted users which contains all_users but none in untrusted_users.

**4-15. Sieve of Eratosthenens:**
Using only a python list, for, in, if, range and remove, write a program that will determine prime numbers between 2 and 1000.
**Algorithm:**
    - List the integers beginning with 2.
    - Circle 2 (it must be a prime) 
    - Cross out all its multiples, they cannot be primes.
    - Circle the next integer that is not yet crossed out cross out its multiples.
    - Repeat.
