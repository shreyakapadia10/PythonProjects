"""
    Here we're splitting data from dash and then passing it to constructor
    Any symbol can be used for splitting data
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
        # Way 1
        # params = string.split('-')
        # return cls(params[0], params[1], params[2])

        # Way 2 --> *args
        return cls(*string.split('-'))


shreya = Employee("Shreya", 8985, "Student")
shivani = Employee("Shivani", 9846, "Data Analyst")
# Here we are using alternative constructor using class method
harshil = Employee.from_dash("Harshil-98469-CA")

print(shreya.print_details())
print(shivani.print_details())
print(harshil.print_details())