# Version 1
toppings = []
print("\nLet's get you your pizza toppings! Enter 'quit' to exit the program.")
new_topping = ''

while new_topping != 'quit':
    new_topping = input("\tEnter the topping you'd like on your pizza:  ")
    new_topping = new_topping.lower()

    if new_topping != 'quit':
        toppings.append(new_topping)
        print(f'\t\tYou added {new_topping} to your pizza.\n')

if toppings != []:
    print(f'\nYour pizza has {toppings} on it.')

print("Thank you for using our service :)\n")

# Version 2
toppings = []
print("\nLet's get you your pizza toppings! Enter 'quit' to exit the program.")
new_topping = ''

while new_topping != 'quit':
    new_topping = input("\tEnter the topping you'd like on your pizza:  ")
    new_topping = new_topping.lower()
    if new_topping == 'quit':
        break
    else:
        toppings.append(new_topping)
        print(f'\t\tYou added {new_topping} to your pizza.\n')

if toppings != []:
    print(f'\nYour pizza has {toppings} on it.')

print("Thank you for using our service :)\n")

# Version 3
toppings = []
print("\nLet's get you your pizza toppings! Enter 'quit' to exit the program.")
new_topping = ''

active = True

while active:
    new_topping = input("\tEnter the topping you'd like on your pizza:  ")
    new_topping = new_topping.lower()
    if new_topping == 'quit':
        active = False
    else:
        toppings.append(new_topping)
        print(f'\t\tYou added {new_topping} to your pizza.\n')

if toppings != []:
    print(f'\nYour pizza has {toppings} on it.')

print("Thank you for using our service :)\n")