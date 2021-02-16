"""
1. List Comprehension
2. Dictionary Comprehension
3. Set Comprehension
4. Dictionary Comprehension
"""

# Without List comprehension
lst = []

for i in range(100):
    if i % 3 == 0:
        lst.append(i)
print(lst)

# With List Comprehension
# [] is used for lists
divisible_by_3 = [i for i in range(100) if i % 3 == 0]
print(divisible_by_3)


# Dictionary Comprehension
# {key: value} is used for dictionaries
item_dict = {i: f'Item {i}' for i in range(1, 11)}
print(item_dict)

reverse_item_dict = {value: key for key, value in item_dict.items()}
print(reverse_item_dict)


# Set Comprehension
# {} is used for sets
dresses = {dress for dress in ['dress 1', 'dress 2', 'dress 3', 'dress 1', 'dress 2', 'dress 2']}
print(type(dresses))
print(dresses)

# Generator Comprehension
# () is used for generators
gen = (i for i in range(100))
print(type(gen))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())