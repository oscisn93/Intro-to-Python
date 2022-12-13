from dataclasses import dataclass


@dataclass
class User:
    username: str
    age: int
    password: str


def create_user():
    print('Follow the prompt instructions to create your account:')
    complete = False
    while not complete:
        try:
            uname = str(input("Enter a username: "))
            age = int(input("Please enter your age (must be a whole number): "))
            password = str(input("Enter a password: "))
        except ValueError:
            print('The last entry was invalid!')
        else:
            complete = True

    user = (uname, age, password)
    print(f'Created new user with attribnutes: {user}')


create_user()
