import random

def heitto():
    tulos = random.randint(1,6)
    return tulos

tulos = heitto()
print(tulos)

while tulos != 6:
    tulos = heitto()
    print(tulos)

