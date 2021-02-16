# Lists are Mutable
numbers = [5, 9, 6, 3, 1]

print(numbers[:])
print(numbers[::2])
print(numbers[::-1])

# Appends to list
numbers.append(52)
print(numbers)

# Inserts at specified index
numbers.insert(2, 10)
print(numbers)

# Removes specified number
numbers.remove(3)
print(numbers)

# Removes/Pops last number
numbers.pop()
print(numbers)

# Sorts list - Changes lists (doesn't create new list)
numbers.sort()
print(numbers)

# Reverses list - Changes lists (doesn't create new list)
numbers.reverse()
print(numbers)

numbers[2] = 100
print(numbers)

if 2 in numbers:
    print("Yes, 2 is in list")
else:
    print("No, 2 is not in list")

if 100 not in numbers:
    print("Yes, 100 is not in list")
else:
    print("No, 100 is in list")