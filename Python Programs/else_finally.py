f = open("file.txt")

try:
    f1 = open("no_such_file.txt")
    # f1 = open("file2.txt")

except FileNotFoundError as fe:
    print("File not found", fe)

except IOError as e:
    print("IO Error occurred", e)

else:
    print("This will be executed only when except is not executed")

finally:
    print("This will be executed no matter what")
    f.close()