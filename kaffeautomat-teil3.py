

# print("Herzlich Willkommen beim Kaffee-Automaten!")
# print("Bitte wählen Sie aus:")
# print("(k) Kaffee") # \n -> macht eine neue Zeile
# print("(e) Espresso")
# print("(s) Service-Mode")
# auswahl = input()
# print(f"Sie haben sich für Auswahl {auswahl} entschieden.")

# if auswahl == "k":
#    print("Sie haben sich für die Auswahl Kaffee entschieden.")
# elif auswahl == "e":
#    print("Sie haben sich für die Auswahl Espresso entschieden.")
# else:
#    print("Sie haben sich für die Auswahl Service-Mode entschieden.")


## Kaffeeautomat Teil 3

# Vorratsmengen
kaffee_bohnen = 1000
espresso_bohnen = 1000
wasser = 5000
milch = 1000
zucker = 500

# Eine Tasse :
kaffee_pulver = 5
espresso_pulver = 5
wasser_kaffee = 125
wasser_espresso = 25
zucker_tasse = 3
milch_tasse = 30

# Preise :
grundpreis = 1.0
aufpreis = 0.1

print("Herzlich Willkommen beim Kaffee-Automaten!")

while True:
    print("Herzlich Willkommen beim Kaffee-Automaten!")
    print("Preis pro Tasse: ")
    print("Kaffee oder Espresso: 1 Euro")
    print("Milch oder Zucker: 0.1 Euro")

    print("Bitte wählen Sie aus:")
    print("(k) Kaffee")
    print("(e) Espresso")
    print("(s) Service-Mode")

# Auswahl
    auswahl = input("Ihre Auswahl: ")
    if auswahl == "k":
        print("Sie haben sich für die Auswahl Kaffee k entschieden")
        auswahl_zucker = input("Möchten Sie Zucker (j/n)? :")
        if auswahl_zucker == "j":
            print("Sie haben sich für Zucker entschieden")
        elif auswahl_zucker == "n":
            print("Sie möchten keinen Zucker")
        else:
            print("Falsche Eingabe")
            taste = input("Drücken Sie eine beliebige Taste: ")
            continue
        auswahl_milch = input("Möchten Sie Milch (j/n) :")
        if auswahl_milch == "j":
            print("Sie haben sich für Milch entschieden")
        elif auswahl_milch == "n":
            print("Sie möchten keine Milch")
        else:
            print("Falsche Eingabe")
            taste = input("Drücken Sie eine beliebige Taste: ")
            continue

# Mengen
        if kaffee_pulver > kaffee_bohnen:
            print("Vorgang abgebrochen! Unzureichender Vorrat von Kaffee Bohnen")
            taste = input("Drücken Sie eine beliebige Taste: ")
            continue
        elif wasser_kaffee > wasser:
            print("Vorgang abgebrochen! Unzureichender Vorrat von Kaffee Bohnen")
            taste = input("Drücken Sie eine beliebige Taste: ")
            continue
        elif auswahl_zucker == "j":
            if zucker_tasse > zucker:
                print("Vorgang abgebrochen! Unzureichender Vorrat von Kaffee Bohnen")
                taste = input("Drücken Sie eine beliebige Taste: ")
                continue
        elif auswahl_milch == "j":
            if milch_tasse > milch:
                print("Vorgang abgebrochen! Unzureichender Vorrat von Kaffee Bohnen")
                taste = input("Drücken Sie eine beliebige Taste: ")
                continue

# Preis
        getränkepreis = grundpreis
        if auswahl_zucker == "j":
            getränkepreis += aufpreis
        elif auswahl_milch == "j":
            getränkepreis += aufpreis
        else:
            print(f"Bitte {getränkepreis}€ eingeben und ENTER drücken")
        geldbetrag = input()
        if geldbetrag > str(getränkepreis):
            print("Ihr Getränk wird zubereitet")
            print(f"Bitte {geldbetrag - getränkepreis}€ Rückgeld und das Getränk entnehmen und eine Taste drücken")
            taste = input()
            continue
        elif geldbetrag < str(getränkepreis):
            print("Zu wenig Geld, Bestellung abgebrochen \n Drücken Sie eine beliebige Taste")
            taste = input()
            continue

        kaffee_bohnen -= kaffee_pulver
        wasser -= wasser_kaffee
        if auswahl_zucker == "j":
            zucker -= zucker_tasse
        elif auswahl_milch == "j":
            milch -= milch_tasse


    elif auswahl == "e":
        print("Sie haben sich für die Auswahl Espresso e entschieden")



    elif auswahl == "s":
        print("Service-Interface")
        print("----------------------------")
        print("Noch vorhandene Mangen:")
        print(f"Kaffee: {kaffee_bohnen}g , Milch: {milch}ml")
        print(f"Espresso: {espresso_bohnen}g , Wasser: {wasser}ml")
        print(f"Zucker: {zucker}g")

        print("----------------------------")
        print("Mengen pro Tasse:")
        print(f"Kaffee: {kaffee_pulver}g , Milch: {milch_tasse}ml")
        print(f"Espresso: {espresso_pulver}g , Wasser für Kaffee: {wasser_kaffee}ml")
        print(f"Zucker: {zucker_tasse}g , Wasser für Espresso {wasser_espresso}ml")

        print("----------------------------")
        taste = input("Drücken Sie eine beliebige Taste: ")
        continue

    else:
        continue















