import random, json
from peli import Peli

with open("tallennukset.json", "r") as tiedosto:
    tallennus_data = json.load(tiedosto)
if not tallennus_data:
    tallennus_data = {"tallennustila": "tyhjä"}
    with open("tallennukset.json", "w") as tiedosto:
        json.dump(tallennus_data, tiedosto)

pelaajan_nimi = input("Kerro pelaajan nimi:\n")
pelaajan_ika = float(input("\nKerro pelaajan ikä:\n"))

if pelaajan_ika < 12:
    print("\nPelaaja on alaikäinen.\nSuljetaan peli.")
    quit()

print(f"\nTervetuloa {pelaajan_nimi}!")

input()

peli = Peli(pelaajan_nimi)
