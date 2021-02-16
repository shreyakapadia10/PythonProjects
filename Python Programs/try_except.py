a = input("Enter number 1: ")
b = input("Enter number 2: ")

try:
    print("Sum of", a, "and", b, " is :", int(a) + int(b))

except Exception as e:
    print(e)
