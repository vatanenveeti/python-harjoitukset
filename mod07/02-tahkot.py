import random

def heitto(tahkot):
    tulos = random.randint(1,tahkot)
    return tulos

tahkot = int(input("Monta tahkoa nopassa on? "))

tulos = heitto(tahkot)
print(tulos)

while tulos != tahkot:
    tulos = heitto(tahkot)
    print(tulos)

