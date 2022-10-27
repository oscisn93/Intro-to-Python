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

    except ZeroDivisionError:
        print("Division by zero is not defined")
    except IndexError:
        print("Cannot get index 4 of list x.")

# # After exception handling, execution continues
print("execution continues")
