class Human:
    def __init__(self, sex, age, race, hair, eyes, height, weight):
        self.sex = sex
        self.age = age
        self.race = race
        self.hair = hair
        self.eyes = eyes
        self.height = height
        self.weight = weight

    def describe(self):
        print(f"This human has following characteristics:"
              f"\nsex: {self.sex}"
              f"\nage: {self.age}"
              f"\nrace: {self.race}"
              f"\nhair: {self.hair}"
              f"\neyes: {self.eyes}"
              f"\nheight: {self.height}"
              f"\nweight: {self.weight}")

    def health_category(self):
        if self.age < 70 and self.age > 18:
            print(f"This human in a good condition ")
        elif self.age > 70:
            print(f"This human has health limitations")
        elif self.age < 18:
            print(f"This human is developing ")

    def heights(self):
        if self.height > 171:
            print(f"This human is tall")
        else:
            print(f"this human is not tall")



class Robbots(Human):
    def __init__(self, sex, age, race, hair, eyes, height, weight):
        super().__init__(self, sex, age, race, hair, eyes, height, weight)
        self.materials = iron
        self.software = imax

    def madeof(self):
        print(f"Robbot is made of {self.materials} and it has {self.software} operating system")


my_robbot = Robbots('male', 32, 'russian', 'blond', 'blue', 178, 70)
my_robbot.madeof()


print("+++++++++++++++++++++++++++++++++++++++++++")
ruslan = Human('male', 32, 'russian', 'blond', 'blue', 178, 70)
ruslan.describe()
ruslan.health_category()
ruslan.heights()
