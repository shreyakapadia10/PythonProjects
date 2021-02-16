# Writing into file
f = open("file2.txt", "w")
f.write("This is a new file created using python")
f.close()

# Appending into file
f = open("file2.txt", "a")
characters_written = f.write("\nThis will be appended into new line")
print(characters_written, "characters written to file.")
f.close()

# Opening file for read and write both using r+ -> it'll throw error if file doesn't exist
f = open("file3.txt", "r+")
contents = f.read()
print(contents)
f.write("\nr+ will throw error if the file doesn't exist")
f.close()

# Opening file for read and write both using w+ -> it'll not throw error if file doesn't exist,
# but it'll wipe out it's old contents

f = open("file4.txt", "w+")
contents = f.read()
print(contents)
f.write("This file is opened in w+ mode.\n")
f.write("It is created using Python.\n")
f.write("w+ will not throw any error if the file doesn't exist\n")
f.close()