name = "Shreya"
bdate = 10

# Way 1
print("This is %s, my birthdate is %s" % (name, bdate))

# Way 2
print("This is {}, my birthdate is {}".format(name, bdate))
print("My Birthdate is {1}, this is {0}".format(name, bdate))

# Efficient way
print(f'This is {name}, my birthdate is {bdate}')