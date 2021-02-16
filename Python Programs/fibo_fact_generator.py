def fact(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    yield f


factorial = fact(5)
print(factorial.__next__())


# 0 1 1 2 3 5 8 13 21
def fibo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    yield a


ans = fibo(5)
print(ans.__next__())