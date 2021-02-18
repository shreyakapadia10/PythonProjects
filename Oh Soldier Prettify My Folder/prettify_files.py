""":
    Take path, file name and file format in function,
    capitalize each file name except for the one's provided in the file_name given as
    second argument
    take file format as third argument e.g. .jpg
    All the files ending with given file format give them file name as 1,2,3,...
"""

import os


def soldier(path, file_name, file_format):
    fname_lst = []
    with open(file_name) as fp:
        lst = fp.readlines()

    os.chdir(path)

    for nm in lst:
        if nm.endswith('\n'):
            nm = nm.replace('\n', '')
        fname_lst.append(nm)

    for file in os.listdir():
        if file not in fname_lst:
            os.rename(file, file.capitalize())

    i = 1
    for file in os.listdir():
        if file.endswith(file_format):
            os.rename(file, str(i) + file_format)
            i += 1
    print("Success!")


if __name__ == '__main__':
    fpath = input("Enter Path: ")
    filename = input("Enter File Name: ")
    fileformat = input("Enter File Format: ")
    soldier(fpath, filename, fileformat)