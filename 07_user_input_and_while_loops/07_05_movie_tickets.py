age = input('How old are you?  ')

age = int(age)

while age < 3:
    print('Your ticket is $0.')
    break
while age < 13:
    print('Your ticket is $10.')
    break
while age > 12:
    print('Your ticket is $15.')
    break