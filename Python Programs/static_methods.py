"""
    @staticmethod can be used to create static method
    When we don't want to use self or cls
"""


class Employee:
    # Class Variable
    no_of_leaves = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f'My name is {self.name}. I am a {self.role} and my salary is {self.salary}'

    # cls can access class variable only, it refers to the class of the object on which method is called
    @classmethod
    def change_leave(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split('-'))

    @staticmethod
    def print_greetings(string):
        print(string, "Have a nice day! ")


shreya = Employee("Shreya", 8985, "Student")

# Here we are using alternative constructor using class method
harshil = Employee.from_dash("Harshil-98469-CA")

print(shreya.print_details())
shreya.print_greetings('Good Morning!')