import json

from pelaaja import Pelaaja
from maailma import Alue, Maailma

class Peli:

    def __init__(self, pelaajan_nimi):
        self.maailma = Maailma()
        
        self.pelaaja = Pelaaja(pelaajan_nimi, self.maailma.aloitus_alue)

        self.intro()
        input()
        self.päävalikko()

    def intro(self):
        with open("intro.txt", "r", encoding="utf-8") as tiedosto:
            intro_teksti = tiedosto.read()
            print(intro_teksti)

    def tarkista_komento(self,komento, mahdolliset_komennot):
        while komento not in mahdolliset_komennot:
            komento = input("Virheellinen komento, anna uusi.\n")
        return komento

    def päävalikko(self):
        print("Päävalikko\n1. Aloita\n2. Ohjeet\n3. Lopeta")
            
        komento = input("\nKirjoita valinnan numero.\n")
        komento = self.tarkista_komento(komento, ["1","2","3"])

        if komento == "1":
            print()
            self.aloitussivu()
        if komento == "2":
            self.ohjeet()
        if komento == "3":
            self.lopeta()

    def lopeta(self):
        print("Suljetaan peli.")
        quit()

    def ohjeet(self):
        print()
        with open("ohjeet.txt", "r", encoding="utf-8") as ohje:
            ohje_teksti = ohje.read()
            print(ohje_teksti)
        print("\nPalataan päävalikkoon.")
        input()
        self.päävalikko()

    def aloitussivu(self):
        print("Valitse toiminto.")
        print("1. Uusi peli\n2. Lataa peli\n3. Takaisin")

        komento = input("\nValinta: ")
        komento = self.tarkista_komento(komento, ["1","2","3"])

        if komento == "1":
            self.uusi_peli()
        if komento == "2":
            self.lataa_peli()
        if komento == "3":
            self.päävalikko()

    def uusi_peli(self):
        with open("tallennukset.json", "r") as tiedosto:
            tallennus_data = json.load(tiedosto)
        if tallennus_data["tallennustila"] == "täysi":
            print("\nUusi peli korvaa aikaisemman tallennuksen.\nHaluatko varmasti jatkaa?\n1. Kyllä\n2. Ei")

            komento = input("\nValinta: ")
            komento = self.tarkista_komento(komento, ["1","2"])
            
            if komento == "1":
                self.aloita_peli()
            if komento == "2":
                self.aloitussivu()
        else:
            self.aloita_peli()

    def lataa_peli(self):
        with open("tallennukset.json", "r") as tiedosto:
            tallennus_data = json.load(tiedosto)
        if tallennus_data["tallennustila"] == "täysi":
            for alue in self.maailma.alueet:
                if alue.nimi == tallennus_data["pelaaja"]["sijainti"]:
                    sijainti = alue
            self.pelaaja = Pelaaja(tallennus_data["pelaaja"]["nimi"],sijainti)
            self.pelin_kierto()
        else:
            print("Aikaisempaa tallennusta ei ole. Palataan takaisin.")
            input()
            self.aloitussivu()

    def tallenna_peli(self):

        nykyinen_sijanti = self.pelaaja.sijainti.nimi

        with open("tallennukset.json", "r") as tiedosto:
            tallennus_data = json.load(tiedosto)
            tallennus_data = {"tallennustila": "täysi",
                            "pelaaja": {
                                    "nimi": self.pelaaja.nimi,
                                    "sijainti": nykyinen_sijanti,
                                    }}
            
        with open("tallennukset.json", "w") as tiedosto:
            json.dump(tallennus_data, tiedosto, indent=4)
        print("Tallennettu onnistuneesti.")
        
    def aloita_peli(self):
        print("Peli alkaa...")
        input()
        print("Hrrrr, Sakarilla on kylmä.")
        input()
        print("Sakari muistaa omistavansa ihanan lämpimän villapaidan.")
        input()
        print("Mutta missä se on?")
        input()
        print("Aika lähteä etsimään sitä!")
        input()
        self.pelin_kierto()

    def pelin_kierto(self):
        pelitilanne = "kesken"
        while pelitilanne != "läpi":
            self.käynnistä_alue(self.pelaaja.sijainti)

            
            
    def käynnistä_alue(self,alue):
        alue.esittele_alue()
        input()
        if len(alue.seuraavat_alueet) > 1:
            print("Minkä suunnan valitset?")
            nro = 1
            for seuraava in alue.seuraavat_alueet:
                print(f"{nro}. {seuraava.nimi}")
                nro += 1
            print(f"{nro}. Tallenna ja lopeta.")
            
            komento = input("\nValinta: ")
            komento = self.tarkista_komento(komento, ["1","2","3"])
            
            if komento == "1":
                self.pelaaja.liiku(alue.seuraavat_alueet[0])
            if komento == "2":
                self.pelaaja.liiku(alue.seuraavat_alueet[1])
            if komento == "3":
                self.tallenna_peli()
                self.lopeta()
        else:
            self.pelaaja.liiku(alue.seuraavat_alueet[0])
        

