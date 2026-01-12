
messwerte = [99.975,
100.002,
99.999,
99.982,
100.1,
100.009,
99.826,
100.547,
100.023,
100.008]

N = len(messwerte)

# Berechnung des Mittelwerts

summe = 0.0

for x in messwerte:
    summe += x

M = summe / N

# Berechnung der Varianz
var_summe = 0.0

for x in messwerte:
    var_summe += (x - M) ** 2

V = var_summe / (N-1)

print("Messwerte [m]")
print("----------")
for x in messwerte:
    print(x)

print(f"Mittelwert = {M:.3f}m")
print(f"Varianz = {V:.7f} quadratmeter")


