## B.4.1.7 Typumwandlung

laenge = 100.05
print(type(laenge))
l = int(laenge)
print(l)
print(type(l))

zeichen = str(l)
print(zeichen)

text = "Hallo zusammen "

print( text + str(laenge) )
