from pathlib import Path
# Access txt file
path = Path('learning_python.txt')
contents = path.read_text()

print(contents)
# Store lines in list
lines = []
lines.append(contents.splitlines())
# Print contents line by line
for line in lines:
    print(line)