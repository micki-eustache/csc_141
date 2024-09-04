guests = ['alourdes', 'donald', 'tyler']

invite0 = f"{guests[0].title()}, come join me for dinner!"
invite1 = f"{guests[1].title()}, come join me for dinner!"
invite2 = f"{guests[2].title()}, come join me for dinner!"

print(invite0,'\n',invite1,'\n',invite2)

print(f"Unfortunately, {guests[0].title()} can not make it :(")

guests[0] = "megan"
invite0 = f"{guests[0].title()}, come join me for dinner!"

print(invite0,'\n',invite1,'\n',invite2)
