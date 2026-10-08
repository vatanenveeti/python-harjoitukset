class Maailma:
    def __init__(self):
        self.alueet = []

        #hakee esittelyt tarina-tiedostosta
        with open("tarina.txt", "r", encoding="utf-8") as tiedosto:
            tarina = tiedosto.read()

        esittelyt = tarina.split("\n\n")
        #luodaan aloitustilanne
        self.aloitus_alue = Alue("Talo", esittelyt[0])
        self.alueet.append(self.aloitus_alue)

        self.alueet.append(Alue("Etuovi", esittelyt[1]))
        self.alueet.append(Alue("Takaovi", esittelyt[2]))

        self.alueet[0].määrittele_alueet([self.alueet[1],self.alueet[2]])
        #luodaan etuovireitti
        self.alueet.append(Alue("Kylä", esittelyt[3]))
        self.alueet.append(Alue("Pesula", esittelyt[4]))
        self.alueet.append(Alue("Jaskan koti", esittelyt[5]))

        self.alueet[1].määrittele_alueet([self.alueet[3]])
        self.alueet[3].määrittele_alueet([self.alueet[4], self.alueet[5]])
        #pesula
        self.alueet.append(Alue("Sakari ottaa nahkatakin", esittelyt[6],"kyllä"))
        self.alueet.append(Alue("Sakari ei ota nahkatakkia", esittelyt[7],"kyllä"))

        self.alueet[4].määrittele_alueet([self.alueet[6], self.alueet[7]])
        #jaskan koti
        self.alueet.append(Alue("Sakari lähtee roskikselle", esittelyt[8],"kyllä"))
        self.alueet.append(Alue("Sakari hyväksyy tilanteen", esittelyt[9],"kyllä"))

        self.alueet[5].määrittele_alueet([self.alueet[8], self.alueet[9]])
        #luodaan takaovireitti
        self.alueet.append(Alue("Metsä", esittelyt[10]))
        self.alueet.append(Alue("Sakari koputtaa mökin ovea", esittelyt[11]))
        self.alueet.append(Alue("Sakari jatkaa matkaa", esittelyt[12]))

        self.alueet[2].määrittele_alueet([self.alueet[10]])
        self.alueet[10].määrittele_alueet([self.alueet[11], self.alueet[12]])
        #mökki
        self.alueet.append(Alue("Sakari seuraa noitaa", esittelyt[13],"kyllä"))
        self.alueet.append(Alue("Sakari ei seuraa noitaa", esittelyt[14],"kyllä"))

        self.alueet[11].määrittele_alueet([self.alueet[13], self.alueet[14]])
        #lampi
        self.alueet.append(Alue("Sakari alkaa kalastamaan", esittelyt[15],"kyllä"))
        self.alueet.append(Alue("Sakari ei kalasta", esittelyt[16],"kyllä"))

        self.alueet[12].määrittele_alueet([self.alueet[15], self.alueet[16]])


class Alue:
    def __init__(self, nimi, esittely, viimeinen_alue="ei"):
        self.nimi = nimi
        self.esittely = esittely
        self.viimeinen_alue = viimeinen_alue
        self.seuraavat_alueet = []

    #tulostaa alueen tekstin
    def esittele_alue(self):
        print(self.esittely)

    #määrittelee alueen seuraavat alueet
    def määrittele_alueet(self, alueet):
        for alue in alueet:
            self.seuraavat_alueet.append(alue)

