# file_reader.py
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)

# pi_string.py
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))