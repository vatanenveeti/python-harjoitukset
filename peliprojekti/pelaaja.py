class Pelaaja:
    def __init__(self, nimi, ikä, esineet, sijainti, elämäpisteet):
        self.nimi = nimi
        self.ikä = ikä
        self.esineet = esineet
        self.sijainti = sijainti
        self.hp = elämäpisteet

    def liiku(self, kohde):
        self.sijainti = kohde

    def lisää_esine(self, esine):
        self.esineet.append(esine)
