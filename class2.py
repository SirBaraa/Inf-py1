class Student:
    def vorstellen(self):
        print(f"Ich heiße {self.name} und studiere {self.fach}")


student1 = Student()
student1.name = "Baraa"
student1.fach = "Medizinphysik"

student1.vorstellen()


print("--------------------------")

class Studentx:
    def __init__(self, name, fach):
        self.name = name
        self.fach = fach

    def vorstellenx(self):
        print(f"Ich heiße {self.name} und studiere {self.fach}")

student2 = Studentx("Ahmad","Medizin")
student2.vorstellenx()