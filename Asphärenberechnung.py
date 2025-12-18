## B.4.2.2 Asphärenberechnung


import math

# a = 25
# b = 5
# wurzel_a = int(math.sqrt(a))
# print(int(wurzel_a))
# print(wurzel_a)


# potenz_ab = math.pow(5,25)
# potenz_cd = math.pow(2,4)
# print(potenz_ab)
# print(potenz_cd)

print(" ----------------------- ")

# Konstanten definieren

R0 = 40.0
k = -1.01
A4 = 2.54e-7
A6 = -1.05e-10

h = float(input("Bitte geben Sie h ein! "))

# Teil 1
zaehler = math.pow(h,2) / R0
wurzel_inhalt = 1 - (1 + k) * math.pow(h/R0, 2)
nenner = 1 + math.sqrt(wurzel_inhalt)

# Teil 2

summe_1 = A4 * math.pow(h, 4)
summe_2 = A6 * math.pow(h, 6)

z = zaehler / nenner + summe_1 + summe_2

print(f"z(h) = {z}")