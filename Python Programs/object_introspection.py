import inspect


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
# print(emp.email)

print(type(emp))

st1 = "This is str1"
st2 = "This is str1"
print(type(st1))
print(id(st1))
print(id(st2))

st2 = "This is str2"
print(id(st1))
print(id(st2))

print(dir(st1))
print("--------------------------------------------------------------------------------------------")
print(dir(emp))
print("--------------------------------------------------------------------------------------------")
print(inspect.getmembers(emp))
print("--------------------------------------------------------------------------------------------")