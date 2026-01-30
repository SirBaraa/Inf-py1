# - list comprehension
# - lambda function
# - lambde mit lists - lambda mit sorted
# - OOP : Objekt Orientierte Programmierung  : Klassen , Objekt , Attributen, Konstruktor


# 1. Thema : list comprehension : um listen kürzer zu schreiben

# numbers = [1,2,3,4,5]
# print(numbers)

zahlen = []
for x in range(5):
    zahlen.append(x)  # list.append(neue Werte)
print(zahlen)

print("-------------------")
zahlen2 = [x for x in range(5)] # - list comprehension : [Ausdruck for Element in range(n)]
print(zahlen2)

print("-------------------")

summe = []
for x in range(5):
    summe.append(x+2)
print(summe)

summe2 = [x+2 for x in range(5)]
print(f"Summe2 {summe2}")

print("-----------------")

summe3 = [x**2 for x in range(10) if x % 2 == 0]
print(summe3)


summe4 = []
for x in range(10):
    if x % 2 ==0:
        summe4.append(x**2)
print(summe4)



# print("Hier ist eine Informatik Aufgabe")list comprehension mit dne Quadratzahlen von 1 bis 16

# Aufgabe : Erstelle mit
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
 ##   numbers = [x**2 for x in numbers]
#    print(numbers)

print("Methode 1")

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
numbers_quadrat = []
for x in numbers:
    numbers_quadrat.append(x**2)
print(numbers_quadrat)

print("Methode 2")

list = []
for x in range(1,17):
    list.append(x**2)
print(list)

print("Methode 3")

list2 = [ x**2 for x in range(1,17)]
print(list2)

# list =  [ Operation for x in range(n) if ---  ]



# Thema 2 : lambda : um functions kürzer zu schreiben

# def name(parameter):
 #   print(f"hallo{parameter}")

# def summe(x,y):
 #   return x + y

def gruss(name):
    print(f"Hallo {name}")
gruss("Baraa")

def quadrat(x):
    return x**2
zahl = quadrat(5)
print(zahl)

zahl2 = lambda x: x**2 # variable : ein Wert
print(zahl2(4))

print(f"Das ist eine Zahl {zahl2(10)}")


def summe(a,b):
    return a + b

# Schreibe diese Funktion mit lambda

summe = lambda a,b : a + b
print(summe(5,9))

print("-------------------------------------------")
print("------- lambda mit if else Sätzen -----------")

gerade_zahlen = lambda x : "gerade" if x % 2 == 0 else "ungerade"
# variable = lambda x : befehl if x % 2 == 0 else befehl2
print(gerade_zahlen(154))


def gerade_zahlen(x):
    if x % 2 == 0:
        print("gerade")
    else:
        print("ungerade")

print(gerade_zahlen(99))


print("-------------lambda mit lists --------------")

#zahlen5 = [1,2,3,4,5]
#quadrat = list[map(lambda x : x**2, zahlen5)] # 1, 4, 9, 16, 25
#print(quadrat)




print("-------- lambda mit sorted()----------------")


list5 = [4,3,12,7,35,76] # 1D
print(sorted(list5))
print(len(list5))

list6 = [
    [[4,83],
     [65,23]],
    [[4,34],
     [65,45]]
] # 2D , 3D



print(sorted(list6))
print(sorted(list6, key= lambda x: x[1]))

obst = ["Apfel", "Banane", "Wassermelone", "Orange", "Kiwi"]
print(sorted(obst))
sorted_obst = sorted(obst, key= lambda x: len(x))
print(sorted_obst)

# variable = sorted( list, key = lambda x : kriterium )

# Eine einfache 3D-Liste (3 Ebenen)
dreid_liste = [
    [   # Ebene 1
        [1, 2, 3],
        [4, 5, 6]
    ],
    [   # Ebene 2
        [7, 8, 9],
        [10, 11, 12]
    ],
    [   # Ebene 3
        [13, 14, 15],
        [16, 17, 18]
    ]
]

print(dreid_liste[0][1][2])  # Zugriff: Ebene 1 → Zeile 2 → Element 3 → Ausgabe: 6
print(sorted(dreid_liste, key = lambda x: x[2][0]))

