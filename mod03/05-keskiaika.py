leiviskat = input("Anna leiviskät.\n")
naulat = input("\nAnna naulat.\n")
luodit = input("\nAnna luodit.\n")

leiviskat = float(leiviskat)
naulat = float(naulat)
luodit = float(luodit)

massa = ((leiviskat * 20 + naulat) * 32 + luodit) * 13.3

kilot = massa // 1000
grammat = massa % 1000

print(f"\nMassa nykymittojen mukaan: \n{kilot:.0f} kilogrammaa ja {grammat:.2f} grammaa.")
