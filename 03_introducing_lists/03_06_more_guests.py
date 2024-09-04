guests = ['megan', 'donald', 'tyler']

guests.insert(0, 'alex')
guests.insert(2, 'astra')
guests.append('maggie')

invite0 = f"{guests[0].title()}, come join me for dinner!"
invite1 = f"{guests[1].title()}, come join me for dinner!"
invite2 = f"{guests[2].title()}, come join me for dinner!"
invite3 = f"{guests[3].title()}, come join me for dinner!"
invite4 = f"{guests[4].title()}, come join me for dinner!"
invite5 = f"{guests[5].title()}, come join me for dinner!"

print(invite0,'\n',invite1,'\n',invite2,'\n',invite3,'\n',invite4,'\n',invite5)