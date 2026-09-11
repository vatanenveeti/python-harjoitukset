import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus 
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
        return

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit
        return

autot = []
for i in range(10):
    i += 1
    autot.append(Auto(f"ABC-{i}", random.randint(100,200)))

suurin_matka = 0
voittaja = ""

while suurin_matka < 10000:
    for i in range(10):
        autot[i].kiihdytä(random.randint(-10, 15))
        autot[i].kulje(1)
        if autot[i].kuljettu_matka > suurin_matka:
            suurin_matka = autot[i].kuljettu_matka
            voittaja = autot[i].rekisteritunnus

print(f"kilpailun voitti: {voittaja}")

for i in range(10):
    print(f"\nRekisteritunnus: {autot[i].rekisteritunnus}")
    print(f"Huippunopeus: {autot[i].huippunopeus}")
    print(f"Tämänhetkinen nopeus: {autot[i].nopeus}")
    print(f"Kuljettu matka: {autot[i].kuljettu_matka}")
    i += 1


