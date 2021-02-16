def func1():
    print("This is a function")


# Even though we delete func1, a copy will be stored in func2
func2 = func1
del func1
func2()

"""Returning Function via Function"""


def func_ret(num):
    if num == 0:
        return print
    if num == 1:
        return sum


print(func_ret(0))
print(func_ret(1))

"""Executing functions via parameters given in function"""


def executioner(func):
    func("This is an example of passing function in parameter and executing it inside another function.")


executioner(print)

"""Decorator functions"""
# The use here is if we want to perform the same task with many function than
# we can use decorator function


def decorator_func(function):
    def exec_now():
        print("Executing..")
        function()
        print("Executed..")
    return exec_now


@decorator_func
def hi_shreya():
    print("Hi Shreya! This is an example of decorator function.")


# Way 1
# hi_shreya_var = decorator_func(hi_shreya)
# hi_shreya_var()

# Way 2
"""write @decorator_func() before the function whom you want as a decorator"""
hi_shreya()