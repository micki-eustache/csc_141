sandwich_orders = ['ham', 'turkey', 'tuna', 'chicken', 'pastrami', 'pastrami', 
                   'pastrami']
finished_sandwiches = []

print('No pastrami :(')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Your {current_sandwich} is finished.')
    finished_sandwiches.append(current_sandwich)

print(finished_sandwiches)