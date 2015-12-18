# Driver class will have the following methods:
#
# __init__ takes name, car (which is an object from Car class)
# All dunders you need - for example, __str__ would be nice


class Driver:

    def __init__(self, name, car):
        self.__name = name
        self.__car = car

    def __str__(self):
        return 'Name: ' + self.__name + '\n'
        + 'Car: ' + str(self.__car)

    def __repr__(self):
        return self.__str__()

    def get_name(self):
        return self.__name

    def get_car(self):
        return self.car
