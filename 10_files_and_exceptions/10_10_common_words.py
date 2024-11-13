from pathlib import Path


path = Path('paper.txt')
content = path.read_text()

print(f'"the" shows up {content.lower().count('the')} times.')
print(f'The word "the" actually appears {content.lower().count('the ')} times.')