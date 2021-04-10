# 9-3 Users: Make a class called User")


class User:

    def __init__(self, first_name, last_name, occupation, address, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.address = address
        self.phone = phone

    def describe_user(self):
        """print summary of user info"""
        print(self.first_name.title())
        print(self.last_name.title())
        print(self.occupation)
        print(self.address)
        print(self.phone)


    def greet_user(self):
        """Print personalized greeting to a user"""
        print(f"Hello {self.first_name.title()}, nice to see you!")


# create several instances, and use both methods for each:
person1 = User("tom", "jefferson", "programmer", "NYC", "212-0000")
person2 = User("george", "jefferson", "programmer", "NYC", "212-0000")
person3 = User("jessica", "thomson", "programmer", "NYC", "212-0000")

person1.describe_user()
person2.describe_user()
person3.describe_user()

person1.greet_user()
person2.greet_user()
person3.greet_user()

# exe 9.8
print("+++++++++++++++++++9.8 ++++++++++")
#Write a separate Privileges class. The class should have one
#attribute, privileges, that stores a list of strings as described in
#Exercise 9-7.Move the show_privileges() method to this class. Make a
#Privileges instance as an attribute in the Admin class. Create a new
#instance of Admin and use your method to show its privileges."""


class Userlog:
    def __init__(self, first_name, last_name, country, age):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.age = age

    def describe_user(self):
        print(f"Meet our guest {self.first_name.title()} {self.last_name.title()}!"
              f"\n{self.first_name.title()} is {self.age} and lives in {self.country}")

    def greet_user(self):
        print(f"Welcome {self.first_name + ' ' + self.last_name}")


class Privileges:
    def __init__(self, privileges: str):
        self.privileges = privileges

    def show_privileges(self):
        print(f"The user has following privileges: {self.privileges}")


admin_pri = Privileges("can add info, ask questions")


class Admin(Userlog):
    def __init__(self, first_name, last_name, country, age):
        super().__init__(first_name, last_name, country, age)
        self.privileges = admin_pri


user100 = Admin("Jack", "Thompson", "USA", 23)
print(user100.describe_user())
user100.greet_user()
