# Add to the following code such that no unhandled exceptions occur.  
# Look through https://docs.python.org/3/tutorial/errors.htmlLinks to an external site. f
# or example code if you are not sure how to do this.

x = [1,2,3,4]
for i in range(0,3):
    try:
        if i == 0:
            print(y)
        elif i == 1:
            5/0
        else: 
            x[4]
       
# #Multiple except blocks to handle Exceptions            
    except NameError:
        print("Variable not defined")

# # Add handlers for other exceptions

# # After exception handling, execution continues
print("execution continues")
