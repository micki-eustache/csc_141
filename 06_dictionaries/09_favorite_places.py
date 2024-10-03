place1 = {'name': 'NYC'}
place2 = {'name': 'B&N'}
place3 = {'name': 'Theatre'}

person1 = {'first_name': 'Maggie', 'last_name': 'Kline', 'age': 21, 
           'city': 'Glenside', 'fav_place': place2}
person2 = {'first_name': 'Finn', 'last_name': 'Jackson', 'age': 20, 
           'city': 'Madison', 'fav_place': place3}
person3 = {'first_name': 'Jonathan', 'last_name': 'Pensado', 'age': 22, 
           'city': 'Sinking Spring', 'fav_place': place1}

people = [person1, person2, person3]

for person in people:
    print(person)