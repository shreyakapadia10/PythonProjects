"""
    Take input from user, ask user to enter number of items and then create user's choice comprehension
    i.e list, dictionary or set comprehension
"""

n = int(input('Enter number of items: '))

print('1. List Comprehension \n2. Dictionary Comprehension \n3. Set Comprehension')
choice = int(input())

print(f"Enter {n} items separated by comma: ")
items = input().split(', ')

if choice == 1:
    lst = [item for item in items]
    print(lst)
elif choice == 2:
    dictionary = {item: f'Name {item}' for item in items}
    print(dictionary)
else:
    sets = {item for item in items}
    print(sets)