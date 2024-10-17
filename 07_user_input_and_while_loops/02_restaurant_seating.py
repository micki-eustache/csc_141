grp_num = input('\n\nHow many people are in your dinner group?  ')

grp_num = int(grp_num)

if grp_num > 8:
    print('\nPlease wait for a table.\n\n')
else:
    print('\nYour table is ready!\n\n')