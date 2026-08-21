leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("\nAnna naulat.\n")) + leiviskat*20
luodit = float(input("\nAnna luodit.\n")) + naulat*32

massa = luodit * 13.3

kilot = massa // 1000
grammat = massa % 1000

print(f"\nMassa nykymittojen mukaan: \n{kilot:.0f} kilogrammaa ja {grammat:.2f} grammaa.")
