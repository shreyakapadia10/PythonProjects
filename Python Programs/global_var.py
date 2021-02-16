x = 50


def func():
    x = 20

    print("Inside func:", x)


func()
print("Outside func:", x)

y = 60


def func1():
    global y
    y = 70
    print("Changing value of global y")
    print("Inside func1:", y)


func1()
print("Outside func1:", y)

z = 30


def anotherfunc():
    z = 10

    def innerfunc():
        global z
        z = 20

    print("Before calling innerfunc()", z)
    innerfunc()
    print("After calling innerfunc()", z)


print("Before calling anotherfunc()", z)
anotherfunc()
print("After calling anotherfunc()", z)