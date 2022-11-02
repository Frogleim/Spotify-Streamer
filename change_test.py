import json

f = open('./users/data_1.json', 'r+')

f.seek(0)
f.truncate()

data_dict = {"users":[]}
with open('./users/data_1.json', 'w') as updatefile:
    json.dump(data_dict, updatefile)