def uusi_lentoasema(lentoasemat):
    koodi = input("\nUuden lentoaseman ICAO-koodi: ")
    nimi = input("Uuden lentoaseman nimi: ")
    lentoasemat[koodi] = nimi

def hae_lentoasema(lentoasemat):
    koodi = input("\nHaettavan lentoaseman ICAO-koodi: ")
    if koodi in lentoasemat:
        print(f"Lentoaseman nimi on {lentoasemat[koodi]}.")
    else:
        print("Lentoasemaa ei löytynyt.")

print("Valitse alla olevista vaihtoehdoista:\n1. Syötä uusi lentoasema\n2. Hae jo syötetyn lentoaseman tiedot\n3. Lopeta")
komento = int(input("Kirjoita toimintoa vastaava numero: "))

lentoasemat = {"EFHK" : "Helsinki-Vantaan lentoasema"}
while komento != 3:
    if komento == 1:
        uusi_lentoasema(lentoasemat)
    elif komento == 2:
        hae_lentoasema(lentoasemat)
    else:
        print("\nToimintoa ei löytynyt.")

    print("\nValitse alla olevista vaihtoehdoista:\n1. Syötä uusi lentoasema\n2. Hae jo syötetyn lentoaseman tiedot\n3. Lopeta")
    komento = int(input("Kirjoita toimintoa vastaava numero: "))