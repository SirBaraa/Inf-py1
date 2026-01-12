import math


def berechne_kugeldaten(radius: float):
    if radius <= 0:
        var = print("Falsche Zahl")
        return False
    oberflaeche = 4.0 * math.pi * (radius ** 2)
    volumen = (4.0 / 3.0) * math.pi * (radius ** 3)
    print(f"Oberfläche : {oberflaeche}")
    print(f"Volumen : {volumen}")
    return True


berechne_kugeldaten(5.0)





