print('\nEquality tests')
print('BMW' == 'BMW')
print('BMW' == 'bmw')

print('\nInequality with strings tests')
print('south' != 'north')
print('south' != 'south')

print('\n.lower() tests')
car = ['BMW']
print(car[0].lower() == 'bmw')
print(car[0].lower() == 'BMW')

print('\nNumerical equality tests') 
print(9 == 9)
print(9 == 1)

print('\nNumerical inequality tests') 
print(9 != 1)
print(9 != 9)

print('\nNumerical greater than tests') 
print(9 > 1)
print(9 > 9)

print('\nNumerical less than tests') 
print(9 < 10)
print(9 < 9)

print('\nNumerical greater than or equal to tests') 
print(9 >= 1)
print(9 >= 10)

print('\nNumerical less than or equal to tests') 
print(9 <= 10)
print(9 <= 1)

print('\n"and" keyword tests') 
print(9 < 10 and 9 > 1)
print(9 < 1 and 9 > 10)

print('\n"or" keyword tests') 
print(9 < 10 or 9 < 1)
print(9 < 1 or 9 == 10)

print('\nList containing content tests') 
lists = ['ordered', 'unordered']
print ('unordered' in lists)
lists = ['ordered', 'unordered']
print ('bullet' in lists)

print('\nList not containing tests') 
lists = ['ordered', 'unordered']
print ('bullet' not in lists)
lists = ['ordered', 'unordered']
print ('ordered' not in lists)