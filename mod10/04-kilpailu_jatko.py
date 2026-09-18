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

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot_lista):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot_lista

    def tunti_kuluu(self):
        for i in range(len(self.autot)):
            self.autot[i].kiihdytä(random.randint(-10, 15))
            self.autot[i].kulje(1)

    def tulosta_tilanne(self):
        for i in range(len(self.autot)):
            print(f"Rekisteritunnus: {self.autot[i].rekisteritunnus}")
            print(f"Huippunopeus: {self.autot[i].huippunopeus}")
            print(f"Tämänhetkinen nopeus: {self.autot[i].nopeus}")
            print(f"Kuljettu matka: {self.autot[i].kuljettu_matka}\n")
            i += 1

    def kilpailu_ohi(self):
        for i in range(len(self.autot)):
            if self.autot[i].kuljettu_matka >= self.pituus_km:
                return True
        return False

autot = []
for i in range(10):
    i += 1
    autot.append(Auto(f"ABC-{i}", random.randint(100,200)))

kisa = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0
while not kisa.kilpailu_ohi():
    kisa.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        print(f"\nTunteja kulunut {tunnit}\n")
        kisa.tulosta_tilanne()

kisa.tulosta_tilanne()


