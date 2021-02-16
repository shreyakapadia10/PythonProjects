"""1st it checks for instance variable, if not found than class variable will be used"""


class Employee:
    # Class Variable
    no_of_leaves = 10
    
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def print_details(self):
        return f'My name is {self.name}. I am a {self.role} and my salary is {self.salary}'


shreya = Employee("Shreya", 8985, "Student")
shivani = Employee("Shivani", 9846, "Data Analyst")

print(shreya.print_details())
print(shivani.print_details())