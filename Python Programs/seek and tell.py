# Tell tells us the location of where the pointer is f.tell()
# Seek moves the pointer to specified location i.e. f.seek(10)

f = open("file.txt")
print(f.tell())
print(f.readline(), end="")
print(f.tell())
print(f.readline(), end="")
f.seek(0)
print(f.readline(), end="")
f.close()