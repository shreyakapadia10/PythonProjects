lst = ['Shreya','Shivani', 'Harshil', 'Jyoti', 'Dipak']

# Way 1
for name in lst:
    print(name, 'and ', end='')
print('other family members')

# Way 2
joined_names = " and ".join(lst)
print(joined_names, 'and other family members')

# Way 3
print(", ".join(lst), end=' ')