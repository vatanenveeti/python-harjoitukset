import math

def pizza(halkaisija_cm, hinta):
    säde_m = halkaisija_cm/2/100
    pizza_ala = math.pi * säde_m**2
    yksikköhinta = hinta / pizza_ala
    return yksikköhinta

hinta_1 = float(input("Ensimmäisen pizzan hinta(€): "))
halkaisija_1 = float(input("Ensimmäisen pizzan halkaisija(cm): "))
hinta_2 = float(input("Toisen pizzan hinta(€): "))
halkaisija_2 = float(input("Toisen pizzan halkaisija(cm): "))

yksikköhinta_1 = pizza(halkaisija_1, hinta_1)
yksikköhinta_2 = pizza(halkaisija_2, hinta_2)

if yksikköhinta_1 < yksikköhinta_2:
    print("Ensimmäinen pizza on parempi vastine rahalle.")
elif yksikköhinta_2 < yksikköhinta_1:
    print("Toinen pizza on parempi vastine rahalle.")
else:
    print("Pizzat ovat saman arvoiset")