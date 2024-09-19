pizzas = ['cheese', 'mushroom', 'supreme']
friend_pizzas = pizzas[:]

pizzas.append('bacon')
friend_pizzas.append('alfredo')

print('My favorite pizzas are:')
for toppings in pizzas:
    print(toppings)

print("\nMy friend's favorite pizzas are:")
for toppings in friend_pizzas:
    print(toppings)