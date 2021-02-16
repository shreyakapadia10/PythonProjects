"""
    public are the ones that we usually define
    protected can be defined by using one underscore before variable name
    and it can be accessed only by base class and it's child classes
    private can be defined by using double underscores before variable name
    and actually we can access it outside of the class but it'll be in form _classname__variablename
"""


class Employee:
    public = 8
    _protected = 10
    __private = 12

    @property
    def protected(self):
        return self._protected


class Player:
    pass


class CoolProgrammer(Employee):
    pass


emp = Employee()
player = Player()
prog = CoolProgrammer()

# Will generate error as player is not a subclass
# print(player.protected)

# Will not generate error as prog is a subclass
print(prog.protected)

# Will generate error
# print(emp.__private)

# Won't generate error
print(emp._Employee__private)