
grammat = input("Anna grammat: ")
virheellisyys = False

if not grammat.replace(".","").isnumeric():
    virheellisyys = True

if not virheellisyys:
    grammat = float(grammat)
    leiviskat = grammat / 13.3 / 32 // 20
    naulat = grammat / 13.3 // 32 - leiviskat*20
    luodit = grammat / 13.3 - naulat*32 -leiviskat*32*20

    print(f"{grammat} grammaa muutettuna on {leiviskat} leiviskää, {naulat} naulaa ja {luodit} luotia.")
else:
    print("Virheellinen syöte")