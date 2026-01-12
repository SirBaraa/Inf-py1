
messwerte = []
for i in range(10):
    zahl = float(input("Bitte geben Sie eine Zahl ein: "))
    messwerte.append(zahl)

# Berechnung des Mittelwerts

def Mittelwert  (messwerte):
    n = len(messwerte)
    summe = 0.0
    for x in messwerte:
        summe += x
    m = summe / n
    return m

# Berechnung der Varianz

def Varianz(messwerte):

    n = len(messwerte)
    m = Mittelwert(messwerte)
    var_summe = 0.0
    for x in messwerte:
        var_summe += (x - m) ** 2
    v = var_summe / (n-1)
    return v

m = Mittelwert(messwerte)
v = Varianz(messwerte)


print("Messwerte [m]")
print("----------")
for x in messwerte:
    print(x)

print(f"Mittelwert = {m:.3f}m")
print(f"Varianz = {v:.7f} m²")


