num1 = input('Give me a number: ')
num2 = input('Give me another number: ')

try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print('\nI said number, silly :p Try again.')
else:
    print(f'\nYour sum is: {num1 + num2}')