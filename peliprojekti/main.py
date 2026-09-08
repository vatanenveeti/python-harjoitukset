pelaajan_nimi = input("Kerro pelaajan nimi:\n")
pelaajan_ika = float(input("\nKerro pelaajan ikä:\n"))
esinelista = []

if pelaajan_ika < 12:
    print("\nPelaaja on alaikäinen.\nSuljetaan peli.")
    quit()
print(f"\nTervetuloa peliin {pelaajan_nimi}!")

def päävalikko():
    print("Päävalikko\n- Aloita\n- Ohjeet\n- Lopeta")
    
    komento = input("\nValitse ylläolevista vaihtoehdoista.\n")
    komento = komento.lower()

    while not (komento == "aloita" or komento == "ohjeet" or komento == "lopeta"):
        komento = input("Virheellinen komento, anna uusi.\n")
        komento = komento.lower()

    if komento == "aloita":
        aloitussivu()
    if komento == "ohjeet":
        ohjeet()
    if komento == "lopeta":
        lopeta()

def aloitussivu():
    print("\nValitse toiminto.")
    print("- Esineet\n- Tavaraluettelo\n- Jatka")

    komento = input("\nValinta: ")
    komento = komento.lower()

    while not (komento == "esineet" or komento == "tavaraluettelo" or komento == "jatka"):
            komento = input("Virheellinen komento, anna uusi.\n")
            komento = komento.lower()

    if komento == "esineet":
        esineet(esinelista)
    if komento == "tavaraluettelo":
        tavaraluettelo(esinelista)
    if komento == "jatka":
        jatka()
     
def ohjeet():
    print("\nTäältä löytyy ohjeet, mutta niitä ei ole juuri nyt. Palataan päävalikkoon.")
    päävalikko()

def lopeta():
    print("Suljetaan peli.")
    quit()

def esineet(esinelista):
    print("\nKirjoita alle esine, jonka haluat mukaan seikkailulle. Kun et halua enempää, jätä kohta tyhjäksi.")
    esine = input()
    while esine != "":
        esinelista.append(esine)
        esine = input()
    aloitussivu()

def tavaraluettelo(esinelista):
    print("\nLuettelo esineistäsi:")
    for i in esinelista:
        print(i)
    aloitussivu()

def jatka():
    print("Peli jatkuu")

päävalikko()
