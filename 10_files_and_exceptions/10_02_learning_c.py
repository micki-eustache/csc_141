from pathlib import Path
# Access txt file
path = Path('learning_python.txt')
contents = path.read_text()

contents = contents.replace('Python', 'JS')
print(contents)