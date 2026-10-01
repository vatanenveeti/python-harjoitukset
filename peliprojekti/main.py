import random
from pelaaja import Pelaaja
from esine import Esine
from huone import Huone

pelaajan_nimi = input("Kerro pelaajan nimi:\n")
pelaajan_ika = float(input("\nKerro pelaajan ikä:\n"))
esinelista = []
aloitus_huone = Huone("Eteinen")

if pelaajan_ika < 12:
    print("\nPelaaja on alaikäinen.\nSuljetaan peli.")
    quit()

pelaaja = Pelaaja(pelaajan_nimi, pelaajan_ika, esinelista, aloitus_huone, 100)

print(f"\nTervetuloa peliin {pelaaja.nimi}!")

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
        esineet()
    if komento == "tavaraluettelo":
        tavaraluettelo()
    if komento == "jatka":
        jatka()
     
def ohjeet():
    print("\nTäältä löytyy ohjeet, mutta niitä ei ole juuri nyt. Palataan päävalikkoon.")
    päävalikko()

def lopeta():
    print("Suljetaan peli.")
    quit()

def esineet():
    print("\nKirjoita alle esine, jonka haluat mukaan seikkailulle. Kun et halua enempää, jätä kohta tyhjäksi.")
    esineen_nimi = input()
    if esineen_nimi != "":
        esine = Esine(esineen_nimi,random.randint(1,10),random.randint(1,100))

    while esineen_nimi != "":
        pelaaja.lisää_esine(esine)
        esineen_nimi = input()
        if esineen_nimi != "":
            esine = Esine(esineen_nimi,random.randint(1,10),random.randint(1,100))
        
    aloitussivu()

def tavaraluettelo():
    print("\nLuettelo esineistäsi:")
    for i in pelaaja.esineet:
        print(i.nimi)
    aloitussivu()

def jatka():
    print("Peli jatkuu")

päävalikko()
