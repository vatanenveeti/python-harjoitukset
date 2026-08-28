import random

print("Kolminumeroinen koodi:\n", random.randint(0,9), random.randint(0,9), random.randint(0,9))

print("Nelinumeroinen koodi:\n", random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6))

pituus = int(input("Halutun koodin pituus: "))
ensimmainen = int(input("Numerovälin ensimmäinen numero: "))
viimeinen = int(input("Numerovälin viimeinen numero: "))
koodi = ""

i = 0
while i < pituus:
    koodi = koodi + str(random.randint(ensimmainen,viimeinen))
    i = i + 1
print(koodi)