"""
    r = Opens file in read mode = default mode
    w = Opens file in write mode
    x = Creates file if not exists
    a = Appends to file
    t = Opens file in text mode
    b = Opens file in binary mode
    + = Opens file in read and write mode
"""

# File reading and printing entire file using read

print("# File reading and printing entire file using read")
f = open("file.txt")
contents = f.read()
print(contents)
f.close()

print()
print("# File reading and printing some characters of file using read(no of characters)")
print()

# File reading and printing some characters of file using read(no of characters)
f = open("file.txt")
contents = f.read(5)
print(contents)
f.close()

print()
print("# File reading and printing line by line")
print()

# File reading and printing line by line
f = open("file.txt", "rt")
for line in f:
    print(line, end="")
f.close()

print()
print("# File reading and printing using readline(), it will print only one line")
print()

# File reading and printing using readline(), it will print only one line
f = open("file.txt", "rt")
print(f.readline())
f.close()

print()
print("# File reading and printing using readlines(), it will convert file lines into list of lines")
print()

# File reading and printing using readlines(), it will convert file lines into list of lines
f = open("file.txt", "rt")
contents = f.readlines()
print(contents)
f.close()