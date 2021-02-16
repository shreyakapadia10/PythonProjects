class A:
    # Class Variable
    classvar1 = "This is a class variable of class A"

    def __init__(self):
        self.var = "I'm inside class A's constructor"
        # Instance Variable
        self.classvar1 = "This is an instance variable of class A inside constructor"
        self.special = "Special Variable"


class B(A):
    # classvar2 = "This is a class variable 2 of class B"
    classvar1 = "This is a class variable 1 of class B"

    def __init__(self):
        # As we've overridden the constructor of class A we can't access it,
        # to access special instance variable we need to call super().__init__()
        super().__init__()
        self.var = "I'm inside class B's constructor"

        # If we comment the following line than classvar1 of class B will be printed
        # As we've overwritten constructor of class A
        self.classvar1 = "This is an instance variable of class B inside constructor"  # Instance Variable


a = A()
b = B()

# It'll first find instance variable in B, if not found than will search in A for instance variable
print(b.classvar1)

# As we've overridden the constructor of class A we can't access it,
# to access special instance variable we need to call super().__init__()

# It'll print var and classvar1 of B as we've called super().__init__()
# so the variables of class A are overridden

# And if we write super().__init__() at last than var and classvar1 of class A
# will be printed
print(b.special, b.var, b.classvar1)