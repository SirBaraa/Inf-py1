## B.4.1.6 Standardeingabe


vorname = str(input("Bitte den Vornamen eingeben: ")) # str(input())
nachname = str(input("Bitte den Nachnamen eingeben: "))
plz = int(input("Bitte die Postleitzahl eingeben :")) # int()
wohnort = str(input("Bitte den Wohnort eingeben: "))
strasse = str(input("Bitte die Straße eingeben: "))
hausnummer = int(input("Bitte die Hausnummer eingeben: "))

plz_str = format(plz, "05d")
hausnummer_str = str(hausnummer)

ausgabe = (
 vorname +  " " + nachname + "\n" +
 plz_str + " " + wohnort + "\n" +
 strasse + " " + hausnummer_str
)

print(ausgabe)





