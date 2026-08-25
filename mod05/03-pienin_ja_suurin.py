luku = input("Syötä luku. Kun et halua syöttää enempää, syötä tyhjä merkkijono.\n")

suurin = ""
pienin = ""

if luku != "":
    suurin = float(luku)
    pienin = float(luku)

while luku != "":
    luku = float(luku)
    if luku > suurin:
        suurin = luku
    elif luku < pienin:
        pienin = luku
    luku = input("Syötä uusi luku\n")

print(f"Pienin syötetty luku: {pienin}\nSuurin syötetty luku: {suurin}")
