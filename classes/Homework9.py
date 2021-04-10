print("++++++++++++++++9.1++++++++++++++++++++")
""" Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a 
cuisine_type. Make a method called describe_restaurant() that 
prints these two pieces of information, and a method called 
open_restaurant() that prints a message indicating that the 
restaurant is open.
Make an instance called restaurant from your class. 
Print the two attributes individually, and then call both methods."""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} the best place if "
              f"you are looking for {self.cuisine_type} cuisine!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is open!")


my_res = Restaurant("'Hello'", "russian")
my_res.describe_restaurant()
my_res.open_restaurant()

print("++++++++++++++++9.2++++++++++++++++++++")
thai_res = Restaurant("'Budda'", "Thai")
korean_res = Restaurant("'Rice'", "Korean")

thai_res.describe_restaurant()
korean_res.describe_restaurant()

print("++++++++++++++++9.3++++++++++++++++++++")


class Userlog:
    def __init__(self, first_name, last_name, country, age):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.age = age

    def describe_user(self):
        print(f"Meet our guest {self.first_name + ' ' + self.last_name}!"
              f"\n{self.first_name} is {self.age} and lives in {self.country}")

    def greet_user(self):
        print(f"Welcome {self.first_name + ' ' + self.last_name}")


admin = Userlog("john", "Smith", "usa", "25")
admin.describe_user()
admin.greet_user()
user21 = Userlog("Mike", "Paterson", "Canada", "32")
user21.describe_user()
user21.greet_user()

user34 = Userlog("Kate", "Soe", "Egypt", '36')
user34.describe_user()
user34.greet_user()

print("++++++++++++++++9.4++++++++++++++++++++")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} the best place if "
              f"you are looking for {self.cuisine_type} cuisine!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is open!")

    def set_number_served(self, number_served: int):
        self.number_served += number_served
        print(f"We served {self.number_served} customers so far!")

    def increment_number_served(self, customers: int):
        self.number_served += customers
        print(f"We served {self.number_served} customers today!")


indigo = Restaurant("Indigo", "vegan")
print(f"We served {indigo.number_served} customers so far!")
indigo.number_served = 20
print(f"We served {indigo.number_served} customers so far!")
indigo.set_number_served(40)
indigo.increment_number_served(30)

print("++++++++++++++++9.5++++++++++++++++++++")


class User:
    login_attemps = 0  # this i not a parametr = it's variable

    def __init__(self):
        pass  # means do nothing, it is place holder
        self.login_attemps = 0  # inside the function has be self,
        # this is alternate way of creating global variable

    def increment_login_attemps(self):
        self.login_attemps += 1
        print(f"incrementing the value by 1")

    def reset_login_attemps(self):
        self.login_attemps = 0
        print(f"resetting the value to 0")


user1 = User()
user1.increment_login_attemps()
user1.increment_login_attemps()
user1.increment_login_attemps()
user1.increment_login_attemps()
user1.increment_login_attemps()
user1.increment_login_attemps()
print(user1.login_attemps)
user1.reset_login_attemps()

print("++++++++++++++++9.6++++++++++++++++++++")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} the best place if "
              f"you are looking for {self.cuisine_type} cuisine!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is open!")

    def set_number_served(self, number_served: int):
        self.number_served += number_served
        print(f"We served {self.number_served} customers so far!")

    def increment_number_served(self, customers: int):
        self.number_served += customers
        print(f"We served {self.number_served} customers today!")


class Icecream(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", 'chocolate', "green tea", "cherry"]

    def display_flavors(self):
        print(f"We have following flavors: {self.flavors}")


icecream = Icecream("'Sunny Day'", "ice cream")
icecream.display_flavors()
icecream.describe_restaurant()

print("++++++++++++++++9.7++++++++++++++++++++")
class Admin(Userlog):
    def __init__(self, first_name, last_name, country, age):
        super().__init__(first_name, last_name, country, age)
        self.privileges = ["can add post", "can delete post", "can ban user"]


person = Admin("John", "Smith", "USA", "32")
print(person.


print("++++++++++++++++9.8++++++++++++++++++++")
#Write a separate Privileges class. The class should have one
#attribute, privileges, that stores a list of strings as described in
#Exercise 9-7.Move the show_privileges() method to this class. Make a
#Privileges instance as an attribute in the Admin class. Create a new
#instance of Admin and use your method to show its privileges."""


class Privileges:
    def __init__(self, privileges):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"The user has following privileges: {self.privileges}")

class Admin(Userlog):
    def __init__(self, first_name, last_name, country, age):
        super().__init__(first_name, last_name, country, age)
        self.privileges = Privileges()


user100 = Admin("Jack", "Thompson", "USA", 23)
user100.privileges.show_privileges()

print("++++++++++++++++9.9++++++++++++++++++++")
"""Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method 
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and 
then call get_range() a second time after upgrading the battery. You should 
see an increase in the car’s range."""

class Car:
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


class ElectricCar(Car):

    def __init__(self, model, color, brand):  # those paremeters are reqiured  lives only in that fun
        """ This is conctructor, with required parameters"""
        super().__init__(brand, model, color) # call for
        self.battery_size = 60

    def get_battery_info(self):
        print(f"this ia car has a {self.battery_size} kWh bettery")

    def get_description(self):
        """ """
        super().get_description() # inherince paper fun
        print(f"battery size of the car: {self.battery_size}")   # something different

    def drive(self):
        print(f"You are driving el car")
        # we are overting papernt function and dont use super().
