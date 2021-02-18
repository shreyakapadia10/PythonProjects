"""
    If we've a function in which it takes some time for initialization or some file reading functions,
    or anything like that we can you coroutines.
    Here we'll use (yield) inside infinite while loop thus when we call our function it'll take
    time only for the first time for initialization after that for all the rest of the work it
    will start from the next part instead of running initializing all things aagain
"""


def find_name():
    f1 = open("dummy.txt")
    f1_contents = f1.read()

    import time
    time.sleep(5)

    f2 = open("dummy2.txt")
    f2_contents = f2.read()

    time.sleep(5)

    while True:
        name = (yield)

        if name in f1_contents:
            print("Name found in file1")
        elif name in f2_contents:
            print("Name found in file2")
        else:
            print("Name not found")


result = find_name()
next(result)
user_ip = input("Enter name: ")
result.send(user_ip)

user_ip = input("Enter name: ")
result.send(user_ip)

user_ip = input("Enter name: ")
result.send(user_ip)

result.close()