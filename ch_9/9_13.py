from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        print(self.sides,'sided dieroll result:',randint(1, self.sides))

six_sided = Die()
ten_sided = Die(10)
twenty_sided = Die(20)

print('Starting simulations...\n')
for i in range(0, 10):
    six_sided.roll_die()
print('')

for i in range(0, 10):
    ten_sided.roll_die()
print('')

for i in range(0, 10):
    twenty_sided.roll_die()
print('\nSimulation complete!')
