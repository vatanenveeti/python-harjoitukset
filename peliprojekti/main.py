import json
from peli import Peli
#tekee tallennukset-tiedostosta oikean muotoisen, jos se on tyhjä
with open("tallennukset.json", "r") as tiedosto:
    tallennus_data = json.load(tiedosto)
if not tallennus_data:
    tallennus_data = {"tallennustila": "tyhjä"}
    with open("tallennukset.json", "w") as tiedosto:
        json.dump(tallennus_data, tiedosto)

pelaajan_nimi = input("Kerro pelaajan nimi:\n")

print("\nKerro pelaajan ikä:")
while True:
    try:
        pelaajan_ika = float(input(""))
        break
    except ValueError:
        print("Virheellinen komento, anna uusi.")

if pelaajan_ika < 12:
    print("\nPelaaja on alaikäinen.\nSuljetaan peli.")
    quit()

print(f"\nTervetuloa {pelaajan_nimi}!")
input()

#luo peli-olion ja aloittaa itse pelin
peli = Peli(pelaajan_nimi)
