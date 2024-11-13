from pathlib import Path

files = ['cats.txt', 'dogs.txt']

try:
    for file in files:
        path = Path(file)
        content = path.read_text()
        print(content)

except FileNotFoundError:
    print(f'{path} does not exist.')