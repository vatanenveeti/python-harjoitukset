class Maailma:
    def __init__(self):
        self.alueet = []

        aloituksen_esittely =  "Sakari on tutkinut koko talonsa, mutta villapaitaa ei löydy mistään." \
                            "\nVoi Sakaria. Sakari voi jatkaa matkaa ulos etuoven tai takaoven kautta."
        self.aloitus_alue = Alue("Talo", aloituksen_esittely)
        self.alueet.append(self.aloitus_alue)

        etuovi_esittely = "Sakari menee etuovesta etupihalle. Etupiha on tyhjä kuin avaruus. " \
                            "\nSiellä ei ole villapaitaa. Sakari hyppää autoonsa ja lähtee kylää kohti."
        self.alueet.append(Alue("Etuovi", etuovi_esittely))

        takaovi_esittely = "Sakari päätti poistua takaovesta takapihalle. \nHän käy kaikki kivet ja kolot läpi, " \
                            "mutta villapaitaa ei näy missään. Sakaria surettaa. \nTakapihalta Sakari jatkaa matkaansa " \
                            "synkkään metsään."
        self.alueet.append(Alue("Takaovi", takaovi_esittely))

        self.alueet[0].määrittele_alueet([self.alueet[1],self.alueet[2]])


    def hae_aloitus(self):
        return self.aloitus_alue

class Alue:
    def __init__(self, nimi, esittely):
        self.nimi = nimi
        self.esittely = esittely
        self.seuraavat_alueet = []

    def esittele_alue(self):
        print(self.esittely)

    def määrittele_alueet(self, alueet):
        for alue in alueet:
            self.seuraavat_alueet.append(alue)

