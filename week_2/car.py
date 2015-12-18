# Car class will have the following methods:
#
# __init__, which takes car, model and max_speed
# All dunders you need - for example, __str__ would be nice


class Car:

    def __init__(self, car, model, max_speed):
        self.__car = car
        self.__model = model
        self.__max_speed = max_speed

    def __str__(self):
        return 'Car: ' + self.__car + '\n' + 'Model: ' + self.__model
        + '\n' + 'Max speed: ' + str(self.__max_speed)

    def __repr__(self):
        return self.__str__()
