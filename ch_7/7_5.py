print("Enter \"quit\" when finished.\n")
age = ""
while(age != quit):
    age = input("How old are you? ")
    if not age.isdigit() or int(age) < 0:
        print("Invalid age.")
    elif int(age) < 3:
        print("Entry is free.")
    elif int(age) < 12:
        print("Entry is $10.")
    else:
        print("Entry is $15")