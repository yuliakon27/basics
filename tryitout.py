class Userlog:
    def __init__(self, first_name, last_name, country, age):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.age = age

    def describe_user(self):
        print(f"Meet our guest {self.first_name.tittle() + ' ' + self.last_name.tittle()}!"
              f"\n{self.first_name.tiitle()} is {self.age} and lives in {self.country.tittle()}")

    def greet_user(self):
        print(f"Welcome {self.first_name.tittle() + ' ' + self.last_name.tittle()}")

class Privilege:
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        #print(F"this user has following privileges: {self.privileges}")

        if self.privileges:
            for privilege in self.privileges:
               print(privilege)
        else:
            print(f"no privileges")

class Admin(Userlog):
    def __init__(self, first_name, last_name, country, age):
        super().__init__(first_name, last_name, country, age)
        self.privileges = Privilege()




user100 = Admin("Jack", "Thompson", "USA", 23)
user100_pri = ["ask questions", "add value", "change data"]
#object  attribute       action
user100.privileges.privileges = user100_pri
user100.privileges.show_privileges()
