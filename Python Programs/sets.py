"""We can use sets to store unique values and
all the operations such as union,
intersection, etc. can be performed on set"""

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(1)
print(s)

s.remove(2)
print(s)

s1 = {2, 5, 6}  # Also a way to create set

print(s1.union(s))
print(s1.isdisjoint(s))
print(max(s))
print(min(s))
print(len(s))