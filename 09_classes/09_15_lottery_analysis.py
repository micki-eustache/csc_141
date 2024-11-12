from random import choice

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = []
current_ticket = []
count = 0

print('\n\n\nWin a prize if you have a ticket matching:')
for num in range(4):
    winning_ticket.append(choice(list))

print(winning_ticket)

while current_ticket != winning_ticket:
    for num in range(4):
        current_ticket.append(choice(list))
    count += 1
    if current_ticket == winning_ticket:
        break
    else:
        current_ticket.clear()

print(f'\nIt took {count} pulls to get a winning ticket!\n\n\n')