n = int(input("Enter number of rows: "))
b = int(input("Enter 0 or 1: "))

tf = bool(b)

if tf:
    i = 1
    while i <= n:
        print(i * "* ")
        i += 1
else:
    i = n
    while i > 0:
        print(i * "* ")
        i -= 1