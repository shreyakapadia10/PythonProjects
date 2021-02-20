import json

data1 = '{"name" : "Shreya", "surname": "Kapadia"}'
print(data1)
# Here json.loads() will return dictionary so that we can access values using keys,
# but it won't be possible using simple data1 object
# print(data1['name'])

json_data1 = json.loads(data1)
print(json_data1)
print(json_data1['name'])
print(type(json_data1))

data2 = {
    "name": "Shreya",
    "family_members": ["Shreya", "Shivani", "Harshil", "Jyoti", "Dipak"],
    "age": (20, 24, 18, 53, 55),
    "hasUncle": False
}

# Will convert python data into json form
json_data2 = json.dumps(data2)
print(json_data2)

# sorted_keys will sort data in ascending order
alphabets = {
    "S": 24,
    "J": 52,
    "H": 18,
    "D": 53
}

sorted_json = json.dumps(alphabets, sort_keys=True)
print(sorted_json)

numbers = {
    5: 24,
    6: 52,
    1: 18,
    0: 53
}

sorted_json1 = json.dumps(numbers, sort_keys=True)
print(sorted_json1)

print()

# json.load() can be used to read a file containing json
with open("file_json.json") as fp:
    load_json = json.load(fp=fp)
    print(load_json)

# json.dump() can be used to write python objects as JSON in a given file
with open("new_json_file.json", 'a') as fp:
    json.dump(data2, fp=fp)
