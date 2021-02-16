class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # Getter
    @property
    def email(self):
        if self.fname is None or self.lname is None:
            return f"Email not set, try providing values to setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    # Setter
    @email.setter
    def email(self, string):
        print("Setting new email..")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    # Deleter
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

    def explain(self):
        if self.fname is None or self.lname is None:
            return f"First Name and Last name is not set"
        return f"This is {self.fname} {self.lname}"


emp = Employee("Shreya", "Kapadia")
print(f"Before changing First Name: {emp.email}")

# Even after changing fname, the email doesn't change thus we need setter
emp.fname = "ShreyaD"
print(f"After changing First Name: {emp.email}")

# After creating a method named email()
# After we make email() as @property the parenthesis won't be needed
# print(emp.email())

# Now we can call email directly as property
print(emp.email)

# Setter is required because if we write as below, it'll generate error that "can't set attribute"
# emp.email = "shreya@gmail.com"

# Now as the setter is provided we can write as below
emp.email = "ShreyaD.Kapadia@gmail.com"
print(f'New first name after changing email: {emp.fname}')
print(f'New last name after changing email: {emp.lname}')
print(f'New email: {emp.email}')

# Now if we want to delete emp than writing as below will also generate an error
# As deleter is not set
# del emp.email

# Now as the deleter is provided we can write as below
del emp.email
print(emp.email)
print(emp.explain())