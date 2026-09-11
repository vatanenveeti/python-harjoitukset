class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus 
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

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

auto = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {auto.rekisteritunnus}")
print(f"Huippunopeus: {auto.huippunopeus}")
print(f"Tämänhetkinen nopeus: {auto.nopeus}")
print(f"Kuljettu matka: {auto.kuljettu_matka}")

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print(f"Nopeus kiihdytyksen jälkeen: {auto.nopeus}")

auto.kiihdytä(-200)

print(f"Nopeus hätäjarrutuksen jälkeen: {auto.nopeus}")

