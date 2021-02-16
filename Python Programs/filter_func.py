numbers = list(range(0, 10))


def greater_than_5(n):
    return n > 5


# Here we are filtering the numbers greater than 5
# filter function also returns object thus we're typecasting it to list

is_greater_5 = list(filter(greater_than_5, numbers))
print(is_greater_5)

is_less_5 = list(filter(lambda n: n < 5, numbers))
print(is_less_5)