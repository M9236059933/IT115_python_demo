import json

data = {
    'name': 'Anzhello Merkutsio',
    'age': 35,
    'city': 'Seattle, WA',
    'interests': ['Cars', 'Traveling', 'Food', 'Movies'],
    'is_student': True
}

with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print('You have successfully written to data.json')