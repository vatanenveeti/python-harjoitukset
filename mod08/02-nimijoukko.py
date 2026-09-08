nimet = set()

nimi = input("Syötä nimiä: ")
while nimi != "":
    if nimi not in nimet:
        print("Uusi nimi")
        nimet.add(nimi)
    else:
        print("Aiemmin syötetty nimi")
    nimi = input("")

for n in nimet:
    print(n)