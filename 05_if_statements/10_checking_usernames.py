current_users = ['admin', 'mtma0327', 'jaden99', 'gggio', 'yunluvr']

new_users = ['GGgio', 'autvmn', 'jaden99', 'sw4n', 'earl_b']

for user in new_users:
    if user.lower() in current_users:
        print(f'\nUsername "{user}" not availible.\nPlease enter another\n')
    else:
        print(f'\nUsername {user} availible!\n')