pelaajan_nimi = input("Kerro pelaajan nimi:\n")
pelaajan_ika = float(input("\nKerro pelaajan ikä:\n"))

if pelaajan_ika < 12:
    print("\nPelaaja on alaikäinen.\nSuljetaan ohjelma.")
    quit()
print(f"\nTervetuloa peliin {pelaajan_nimi}!")

komento = ""
while komento != "lopeta":

    print("Päävalikko\n- Aloita\n- Ohjeet\n- Lopeta")

    komento = input("\nValitse ylläolevista vaihtoehdoista.\n")
    komento = komento.lower()

    while not (komento == "aloita" or komento == "ohjeet" or komento == "lopeta"):
        komento = input("Virheellinen komento, anna uusi.\n")
        komento = komento.lower()

    if komento == "aloita":
        print("\nPeli alkaa\n.\n..\n...\nEi onnistunut. Palataan päävalikkoon.")
    if komento == "ohjeet":
        print("\nTäältä löytyy ohjeet, mutta niitä ei ole juuri nyt. Palataan päävalikkoon.")
