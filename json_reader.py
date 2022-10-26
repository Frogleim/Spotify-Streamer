import json


file = open('./data.json')

data = json.load(file)
for items in data['users']:
    print(items['email'])