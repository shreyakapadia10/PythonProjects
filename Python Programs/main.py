mystr = "Hello World!"
# Printing entire string
print(mystr[:])

# Skipping 2 characters
print(mystr[::2])

# Reversing String
print(mystr[::-1])

# False due to spaces
print(mystr.isalnum())
mystr = "HelloWorld"
# True as spaces as well as ! are removed
print(mystr.isalnum())

# Checking if str is alpha
print(mystr.isalpha())

# Checking if str ends with orld
print(mystr.endswith("orld"))

# Counting no. of 'o'
print(mystr.count('o'))

# Converting to uppercase
print(mystr.upper())

# Converting to lowercase
print(mystr.lower())

# Converting first letter to capital
print(mystr.capitalize())

# Replacing world by ' world!'
print(mystr.replace('World', ' World!'))