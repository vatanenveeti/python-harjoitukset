def muunnos(gallonat):
    suhde = 3.785
    litrat = gallonat * suhde
    return litrat

gallonat = float(input("Gallonamäärä: "))

while gallonat >= 0:
    litrat = muunnos(gallonat)
    print(f"{gallonat} gallonaa on {litrat} litraa.")
    gallonat = float(input("Gallonamäärä: "))
