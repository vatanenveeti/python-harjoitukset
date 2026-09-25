class Peli:
    def __init__(self, huoneet, aloitus_huone):
        self.huoneet = huoneet
        self.nykyinen_huone = aloitus_huone

    def Pelaa(self):
        käsky = input("Valitse suunta: ")
        while käsky != "q":
            if käsky == "oikea" or "vasen" or "eteen" or "taakse":
                if käsky == "oikea":
                    kohde = self.nykyinen_huone.oikealla
                elif käsky == "vasen":
                    kohde = self.nykyinen_huone.vasemmalla
                elif käsky == "eteen":
                    kohde = self.nykyinen_huone.edessä
                else:
                    kohde = self.nykyinen_huone.takana

                if kohde != "seinä":
                    self.nykyinen_huone = kohde
                    print(f"Olet huoneessa {self.nykyinen_huone.nimi}")
                else:
                    print("Tässä suunnassa on seinä")
            else:
                print('Kirjoita käsky muodossa "oikea", "vasen", "eteen" tai "taakse"')
            käsky = input("Valitse suunta: ")
    
class Huone:
    def __init__(self, nimi, oikealla="seinä", vasemmalla="seinä", edessä="seinä", takana="seinä"):
        self.nimi = nimi
        self.oikealla = oikealla
        self.vasemalla = vasemmalla
        self.edessä = edessä
        self.takana = takana

# Pääohjelma

huoneet = []

