"""
    Iterable = __iter__() or __getitem__()
    Iterator = __next__()
    Iteration = To iterate over

    We can use generator to save memory
"""

# For example consider the following statement
# for i in range(500000):
#     print(i)

# Here the range could be larger, thus consuming more and more memory
# Instead what we'll do is, we'll create a generator, as below
# So the following function will return an object of generator, thus we don't need to store that in memory


def gen(n):
    for i in range(n):
        yield i


g = gen(5000)
print(g)
# We can iterate over generator only once
# Thus when needed we can call __next__() method on the object of generator, as below

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())


# For the string we can't use __next__() method instead we can use iter(string)
# as string is not iterable
# The iteration is automatically handled inside for loop thus it won't give any error of stop iterable
string = "Shreya"
iterator = iter(string)  # Here we are creating iterator on the string and then we can call __next__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())