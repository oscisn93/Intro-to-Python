pizzas = ['pepperoni', 'meat lovers', 'cheese']
friend_pizzas = ['pepperoni', 'meat-lovers', 'cheese']

pizzas.append('thin crust')
friend_pizzas.append('stuffed crust')

print('My favorite pizzas are: ')
for pizza in pizzas:
    print('I like ', pizza, ' pizza.')

print('My friend\'s favorite pizzas are: ')
for pizza in friend_pizzas:
    print('I like ', pizza, ' pizza.')
