import json

pets = {
    'name': 'Charlie',
    'age': 15,
    'meals': ['Purina', 'Hills'],
    'owner': {'fname': 'Bill', 'sname': 'Gates'}
}

with open('pets.json', 'w') as pet_file:
    json.dump(pets, pet_file)

data = json.dumps(pets)

# weekdays = ['Понедельник', 'Вторник','Среда','Четверг','Пятница', 'Суббота','Воскресенье']
#
# st = [i for i in range(1, 6)]
# print(st)
# week_dict = {key: val for key, val in enumerate(weekdays)}
#
# print(week_dict)
#
# data = json.dumps(week_dict)
#
# print(data)
