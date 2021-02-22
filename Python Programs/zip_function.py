lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

# Makes tuple of first value in list1 to first value in list2 and so on..
print(list(zip(lst1, lst2)))

lst1 = [54, 15, 26]
lst2 = [31, 12, 23]
# Sorts list on the basis of first list name passed
print(sorted(zip(lst2, lst1)))