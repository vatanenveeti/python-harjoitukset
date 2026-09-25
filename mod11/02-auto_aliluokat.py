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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, kuljettu_matka=0):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus, kuljettu_matka)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko, kuljettu_matka=0):
        self.tankin_koko = tankin_koko
        super().__init__(rekisteritunnus, huippunopeus, kuljettu_matka)

# Pääohjelma

sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(120)
polttomoottoriauto.kiihdytä(140)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton mittarilukema: {sähköauto.kuljettu_matka} km")
print(f"Polttomoottoriauton mittarilukema: {polttomoottoriauto.kuljettu_matka} km")