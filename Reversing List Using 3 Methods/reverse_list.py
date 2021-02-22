"""
Problem Statement:-
You visited a restaurant called CodeWithHarry,
and the food items in that restaurant are sorted, based on their amount of calories.
You have to reserve this list of food items containing calories.
You have to use the following three methods to reserve a list:

Inbuilt method of python
List name [::-1] slicing trick
Swap the first element with the last one and second element with second last one and so on like,
[6 7 8 34 5] -> [5 34 8 7 6]

Input:
Take a list as an input from the user
[5, 4, 1]

Output:
[1, 4, 5]
[1, 4, 5]
[1, 4, 5]
All three methods give the same results!
"""

numbers = input("Enter a list of calories(separated by space): ")

lst = numbers.split()
lst1 = lst.copy()
lst2 = lst.copy()

# Way 1
lst1.reverse()

# Way 2
reverse_lst2 = lst2[::-1]

# Way 3
i = 0
j = len(lst) - 1

while i != j:
    lst[i], lst[j] = lst[j], lst[i]
    i += 1
    j -= 1

# print(lst1)
# print(reverse_lst2)
# print(lst)

if lst1 == reverse_lst2 == lst:
    print("All the methods gave same result!")