# Adding to a list in different ways
colors = []
colors.insert(0, 'rad')
colors.insert(1, 'yellow')
colors.append('blue')

# Referencing and modifying list items
print(colors[-1].title())
message = f"{colors[0].title()} is the first color on this list. \n Uh oh, typo! Let's fix that."
print(message)
colors[0] = 'red'
print(colors)

# Removing list items
popped_colors = colors.pop(1)
print(f"{popped_colors.title()} is no longer on the list.")
del colors[0]
last_color = 'blue'
colors.remove(last_color)
print(f"The last color to survive was {last_color.lower()}!")

# Sorting
colors = ['red', 'yellow', 'blue']
print(sorted(colors))
print(sorted(colors, reverse=True))
colors.reverse
print(colors)
colors.sort()
print(colors)
colors.sort(reverse=True)
print(colors)
print(len(colors))