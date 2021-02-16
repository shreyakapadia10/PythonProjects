# Using with block will eliminate the need of using f.close()

with open("file.txt", "rt") as f:
    print(f.read())