def add(a, b):
    return a + b


summation = lambda a, b: a + b

print("Using function add:", add(2, 3))
print("Using lambda function: ", summation(2, 3))


def acc_second_sort(l):
    return l[1]

# It will sort according to second element of list of list
lst = [[3, 23], [20, 45], [10, 1]]
lst.sort(key=acc_second_sort)
print(lst)

# It will sort according to second element of list of list
# Same as above but using lambda function
lst1 = [[3, 53], [20, 15], [10, 65]]
lst1.sort(key=lambda s: s[1])
print(lst1)