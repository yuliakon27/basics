# 3/28/2021 Object-oriented programming concepts: Class and object

# class without defining __init__ Python creates it itself
class Car:  # for first class '()' are optional
    """This class describes model of the car"""

    def __init__(self, model, color, brand):  # those paremeters are reqiured  lives only in that fun
        """ This is conctructor, with required parameters"""
        self.model = model  # have to creat global self so it will live outside if this function
        self.color = color
        self.brand = brand
        self.__odo_reader = 0  # value by default, not required, hidden variable,

    def set_odometer_reader(self, miles):
        """Function to update the value of the odo_reader"""
        if miles > self.__odo_reader:
            self.__odo_reader = miles
        else:
            print(f"miles can not be less than odometer")
        self.__odo_reader = miles

    def drive(self):
        """driving action"""
        print(f"You are driving the car!")

    def do_something(self):
        print(f"I want to do something ......")
        print(f"Let me drive this car......")
        self.drive()

    def get_description(self):
        """ """
        # greetins()
        print(f"Model of the car: {self.model}")
        print(f"Color of the car: {self.color}")
        print(f"Brand of the car: {self.brand}")
        print(f"You have {self.__odo_reader} miles on your car")


def greet_user():
    print(f"Hello master")


class ElectricCar(Car):
    """This is the child class of Car. ElCar class unherits from car class"""

    def __init__(self, model, color, brand):  # those paremeters are reqiured  lives only in that fun
        """ This is conctructor, with required parameters"""
        super().__init__(brand, model, color) # call for
        self.battery_size = 60

    def get_battery_info(self):
        print(f"this ia car has a {self.battery_size} kWh bettery")

    def get_description(self):
        """ """
        super().get_description() # inherince parent fun
        print(f"battery size of the car: {self.battery_size}")   # something different

    def drive(self):
        print(f"You are driving el car")
        # we are overting papernt function and dont use super().