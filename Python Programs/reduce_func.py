from functools import reduce

numbers = list(range(1, 6))

# Way 1 --> Less Efficient
summation = 0

for n in numbers:
    summation += n

print(summation)

# Way 2 --> More Efficient
res = reduce(lambda a, b: a + b, numbers)
print(res)

product = reduce(lambda a, b: a * b, numbers)
print(product)