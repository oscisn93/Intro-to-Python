from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print('Result:',randint(1, self.sides))

six_sided = Die()
for i in range(0, 10):
    six_sided.roll_die()