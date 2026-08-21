korkeus = float(input("Mikä on seinän korkeus(m)?\n"))
leveys = float(input("\nMikä on seinän leveys(m)?\n"))
maali = float(input("\nKuinka monta neliömetriä voi maalata litralla maalia?\n"))

pinta_ala = korkeus * leveys
maali_maara = pinta_ala / maali

print(f"\nMaalia tarvitaan {maali_maara:.2f} litraa.")

