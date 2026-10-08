class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti

    #vaihtaa pelaajan sijaintia
    def liiku(self, kohde):
        self.sijainti = kohde
