import random

class Inventaario:
    def __init__(self, toiset_loitsut):
        self.loitsut = ["super tulipallo", "näkymättömyys"]
        self.reppu = {}

        for loitsu in toiset_loitsut:
            self.loitsut.append(loitsu)

    def tavaroita_reppuun(self):
        laadut = ("tarumainen", "hyvä", "toimiva", "heikko", "käyttökelvoton")
        tavara = input("\nLisää tavara reppuun\nTyhjä rivi lopettaa\n")
        while tavara != "":
            laatu = laadut[random.randint(0,4)]
            self.reppu[tavara] = laatu
            tavara = input()

    def näytä_tavarat(self):
        print("Repun sisältö:")
        for tavara in self.reppu:
            print(f"{self.reppu[tavara]} {tavara}")

invi = Inventaario(["salamaisku", "jäädytys"])
invi.tavaroita_reppuun()
invi.näytä_tavarat()
