sandwich_orders = ['ham', 'turkey', 'tuna', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Your {current_sandwich} is finished.')
    finished_sandwiches.append(current_sandwich)

print(finished_sandwiches)