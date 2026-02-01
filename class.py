class Person:
    def __init__(self, name, alter, beruf):
        self.name = name
        self.alter = alter
        self.beruf = beruf
        self.id = id

    def person_data(self):
        print(f"Name: {self.name}")
        print(f"Alter: {self.alter}")
        print(f"Beruf: {self.beruf}")


person1 = Person("Baraa", 25, "Medizintechniker")
person1.person_data()

person2 = Person("Ahmad", 59, "Chirurg")
person2.person_data()

print("--------------------------------------------------")


class Auto:
    def __init__(self, marke, km_stand, preis):
        self.marke = marke
        self.km_stand = km_stand
        self.preis = preis

    def auto_data(self):
        print("Marke: ", self.marke)
        print("km_stand: ", self.km_stand)
        print("preis: ", self.preis)

auto1 = Auto("Audi", 134000, 9750)
auto1.auto_data()

