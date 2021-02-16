"""1st it checks for instance variable, if not found than class variable will be used"""


class Employee:
    # Class Variable
    no_of_leaves = 10


shreya = Employee()
shivani = Employee()

shreya.name = "Shreya"
shreya.role = "Student"
shreya.salary = 9874

shivani.name = "Shivani"
shivani.role = "Employee"
shivani.salary = 7896

print(Employee.no_of_leaves)
print(shreya.__dict__)

# Instance Variable
shreya.no_of_leaves = 12
print(shreya.no_of_leaves)
print(shreya.__dict__)
print(Employee.no_of_leaves)
print(Employee.__dict__)
