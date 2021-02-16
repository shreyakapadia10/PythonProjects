"""
    If met() is not present in either B, C, D then it'll go in A
    If met() is present in A and B then it'll go to B
    If met() is present in A, B and C then it'll go to B as we have given D(B, C) as order
    If met() is present in A, B and C then it'll go to C if we have given D(C, B) as order
    If met() is present in A, B, C, D then it'll go to D
"""


class A:
    def met(self):
        print("Class A method")


class B(A):
    def met(self):
        print("Class B method")


class C(A):
    def met(self):
        print("Class C method")


class D(B, C):
    def met(self):
        print("Class D method")


a = A()
b = B()
c = C()
d = D()

d.met()