from pathlib import Path
import json

path = Path('numbers.json')
fav_num = input('Enter your fav number:  ')
# Save fav_num to json
content1 = json.dumps(fav_num)
path.write_text(content1)

# Read in fav_num to memory
content2 = path.read_text()
saved_fav_num = json.loads(content2)

print(f"Lemme guess, your fav number is {saved_fav_num}.")