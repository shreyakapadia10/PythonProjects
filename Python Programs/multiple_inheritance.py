"""
    Now if we print variable 'var' then it'll first look into the class
    If it can't find there then it'll be searched in Employee first as the order is important
    If we have written like class CoolProgrammer(Player, Employee): then it would look into Player
    Also as Player takes two arguments then while making object we need to pass only two parameters
"""


class Employee:
    var = 8
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


class Player:
    var = 9
    no_of_games_allowed = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_details(self):
        return f'My name is {self.name}. I can play {self.game}'


# Here the order of classes inherited matters
class CoolProgrammer(Employee, Player):
    var = 10
    language = 'C++'

    def print_languages(self):
        print(self.language)


# shreya = Employee("Shreya", 8985, "Student")
# harshil = Employee.from_dash("Harshil-98469-CA")

shivani = CoolProgrammer("Shivani", 7945, "Programmer")
print(shivani.print_details())
shivani.print_languages()

# Now if we print variable 'var' then it'll first look into the class
# If it can't find there then it'll be searched in Employee first as the order is important
# If we have written like class CoolProgrammer(Player, Employee): then it would look into Player
# Also as Player takes two arguments then while making object we need to pass only two parameters
print(shivani.var)