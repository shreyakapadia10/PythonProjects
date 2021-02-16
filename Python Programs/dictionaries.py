dt = {"Shreya": 10, "Shivani": 13, "Harshil": 8}
print(dt)

# New copy of dictionary will be created, so that any changes in dt1 will not be reflected in dt
dt1 = dt.copy()
del dt1["Shreya"]
print(dt)

print(dt.items())
print(dt.keys())
print(dt.values())

# Refers to the same dictionary, so that any changes in dt2 will be reflected in dt
dt2 = dt
# Deletes any given key
del dt2["Shivani"]
print(dt)

dt['Shivani'] = 13
print(dt)

# Gets value of particular key
print(dt.get('Shreya'))

# Updates value of a key, if key doesn't exist it'll be created
dt.update({"Jyoti": 13})
print(dt)