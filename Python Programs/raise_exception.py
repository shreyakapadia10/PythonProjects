name = input("Enter name: ")

if name.isnumeric():
    raise ValueError("Numeric values not allowed")

print(f"Hello {name}")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b == 0:
    raise ZeroDivisionError("Can't divide by zero")

print(f"a/b = {a/b}")

try:
    # print(c)
    pass
except Exception as e:
    raise ValueError("No Such variable")