# Vererbung


class Mensch():
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def vorstellen(self):
        print(f"Ich heiße {self.name} und bin {self.alter} Jahre alt")


class Studenten(Mensch): # Erweiterung der Attributen
    def __init__(self, name, alter, fach, matrikelnummer):
        super().__init__(name, alter)
        self.fach = fach
        self.matrikelnummer = matrikelnummer

    def vorstellen(self):
        print(f"Ich heiße {self.name} und bin {self.alter} Jahre alt. Ich studiere {self.fach} und meine Matrikelnummer ist {self.matrikelnummer}")


# Klasse Student erbt von Klasse Mensch

student1 = Studenten("Baraa", 25, "Medizinphysik", 899234)
student1.vorstellen()


class Wagen():
    def __init__(self, km_stand, preis):
        self.km_stand = km_stand
        self.preis = preis

    def data(self):
        print(f"Der KM-Stand: {self.km_stand} und der Preis ist {self.preis}")


class Zug(Wagen):
    pass

zug1 = Zug(120000, 97000)
zug1.data()


