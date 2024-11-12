from random import choice

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

print('Win a prize if you have matching ticket:')
for num in range(4):
    print(choice(list))

