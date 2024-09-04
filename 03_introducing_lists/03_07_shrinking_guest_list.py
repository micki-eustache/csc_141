guests = ['alex', 'megan', 'astra', 'donald', 'tyler', 'maggie']

print("Due to unforseen circumstances, only 2 people may be hosted for dinner.")

next_time = guests.pop()
print(f"Sorry {next_time.title()}, I can no longer accommodate you for dinner. Please join me next time!")
next_time = guests.pop()
print(f"Sorry {next_time.title()}, I can no longer accommodate you for dinner. Please join me next time!")
next_time = guests.pop()
print(f"Sorry {next_time.title()}, I can no longer accommodate you for dinner. Please join me next time!")
next_time = guests.pop()
print(f"Sorry {next_time.title()}, I can no longer accommodate you for dinner. Please join me next time!")

invite0 = f"{guests[0].title()}, I'd still love for you to join me for dinner!"
invite1 = f"{guests[1].title()}, I'd still love for you to join me for dinner!"

print(invite0,'\n',invite1)

del guests[1]
del guests[0]

print(guests)