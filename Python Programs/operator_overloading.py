class Operations:
    def __init__(self, number, lst):
        self.num = number
        self.lst = lst

    def __lt__(self, other):
        return self.num < other.num

    def __ne__(self, other):
        return self.num != other.num

    def __contains__(self, item):
        return item in self.lst


op1 = Operations(5, [1, 2, 3, 4, 5])
op2 = Operations(10, [10, 20, 30, 40, 50])

print(op1 != op2)
print(op2 < op1)
print(3 in op1.lst)