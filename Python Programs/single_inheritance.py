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


class Programmer(Employee):
    def __init__(self, name, salary, role, languages):
        # Here we should call super so that init of super class is called
        self.name = name
        self.salary = salary
        self.role = role
        self.languages = languages

    def print_prog_details(self):
        return f'Programmer\'s name is {self.name}. The role is {self.role} and salary is {self.salary} ' \
               f'and known languages are {self.languages}'


shreya = Employee("Shreya", 8985, "Student")
harshil = Employee.from_dash("Harshil-98469-CA")

shivani = Programmer("Shivani", 7945, "Programmer", ['Python', 'Java'])
print(shivani.print_prog_details())