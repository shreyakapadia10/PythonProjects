"""
    1st it checks for instance variable, if not found than class variable will be used
    We can define a method as @classmethod just like decorators so that class variable can be accessed
    class method can access class instance variable
    And we can class method using any object or class name
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


shreya = Employee("Shreya", 8985, "Student")
shivani = Employee("Shivani", 9846, "Data Analyst")

print(shreya.print_details())
print(shivani.print_details())

# Employee.change_leave(15) --> can also be used
# This will change no_of_leaves of class, not only of shreya object
shreya.change_leave(12)
print(shreya.no_of_leaves)
print(Employee.no_of_leaves)