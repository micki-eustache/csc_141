from pathlib import Path
import json

try: 
    path = Path('numbers.json')
    content2 = path.read_text()
    saved_fav_num = json.loads(content2)

    print(f'Hello fav number {saved_fav_num}!')
    
except json.decoder.JSONDecodeError:
    fav_num = input('Enter your fav number:  ')

    # Save fav_num to json
    content1 = json.dumps(fav_num)
    path.write_text(content1)

    # Read in fav_num to memory
    content2 = path.read_text()
    saved_fav_num = json.loads(content2)

    print(f"Lemme guess, your fav number is {saved_fav_num}.")