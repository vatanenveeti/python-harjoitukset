luku_1 = int(input("Kerro jokin kokonaisluku: "))
luku_2 = int(input("Kerro toinen kokonaisluku: "))
luku_3 = int(input("Kerro kolmas kokonaisluku: "))

summa = luku_1 + luku_2 + luku_3
tulo = luku_1 * luku_2 * luku_3
keskiarvo = summa / 3

print(f"Lukujen summa: {summa:.2f}")
print(f"Lukujen tulo: {tulo:.2f}")
print(f"Lukujen keskiarvo: {keskiarvo:.2f}")