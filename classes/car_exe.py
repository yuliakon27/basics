# 3/28/2021 Object-oriented programming concepts: Class and object
# this is file foe executing class

from classes.cars_class import Car, ElectricCar




my_car = Car('530x', 'black', 'BMW')  # creating an object
your_car = Car('32', 'white', 'Lexus')  # creating an object

print("+++++++++++++++++++++ my car ++++++++++++++++++++++++++++")
my_car.drive()  # execution

my_car.get_description()
print("+++++++++++++++++++++ your car ++++++++++++++++++++++++++++")
your_car.drive()
your_car.do_something()
your_car.get_description()
your_car.set_odometer_reader(30)
your_car.get_description()
your_car.__odo_reader = 50 # this is direct access
your_car.get_description()

print("++++++++++++++++++++++++")

my_ev = ElectricCar("5", "blue", "TESLA")
# my_ev = ElectricCar("5", "blue", "TESLA", 100) DIDN'T WORK FOR ME???? HAVE TO LOOK UP
my_ev.drive()
my_ev.get_description()
print(f"Battery size is {my_ev.battery_size}")
# Car(state, behavior) -> ElectricCar(state, behavior)

print("++++++++++++++++=new method++++++++++++++")
# we can create new methods
my_ev.get_battery_info()

print('+++++++++++++++++++overriding ++++++++++++++++++')
# override the method that parent had (oops - method overriding)
my_ev.get_description()
my_ev.drive()

