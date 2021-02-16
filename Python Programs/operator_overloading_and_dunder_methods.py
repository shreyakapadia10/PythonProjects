class Employee:
    no_of_leaves = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    @classmethod
    def change_leave(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f'My name is {self.name}. I am a {self.role} and my salary is {self.salary}'


emp1 = Employee("Shreya", 4580, "Student")
emp2 = Employee("Shivani", 6580, "Programmer")

print(emp1 + emp2)

# __str__ is not then __repr__ will be called
print(emp1)

# To call __repr__
print(repr(emp1))