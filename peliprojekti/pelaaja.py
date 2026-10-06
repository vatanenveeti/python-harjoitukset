class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti

    def liiku(self, kohde):
        self.sijainti = kohde

    def lisää_esine(self, esine):
        self.esineet.append(esine)
